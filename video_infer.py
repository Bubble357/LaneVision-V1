import cv2
from ultralytics import YOLO
import time

# 1. 加载模型
model = YOLO('yolov8n-seg.pt')

# 2. 视频输入来源（二选一）
video_path = 'test_video.mp4' 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("⚠️ 未找到视频文件，尝试打开摄像头...")
    cap = cv2.VideoCapture(0)  # 0 代表默认摄像头

if not cap.isOpened():
    print("❌ 无法打开视频或摄像头，请检查设备。")
    exit()

print("✅ 视频/摄像头已开启，按 'q' 键退出窗口")

# 3. 循环处理每一帧
frame_count = 0
fps = 0
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("📹 视频播放完毕或读取失败")
        break

    frame_count += 1

    if frame_count % 1 == 0: 
        # 缩小图片（640 -> 320）
        resized_frame = cv2.resize(frame, (320, 320))
        results = model(resized_frame, imgsz=320, verbose=False)
        annotated_frame = results[0].plot()
        # 把结果放大回原窗口大小以便显示
        display_frame = cv2.resize(annotated_frame, (frame.shape[1], frame.shape[0]))
    else:
        display_frame = frame

    # 计算并显示 FPS（每秒帧数）
    curr_time = time.time()
    if curr_time - prev_time >= 1.0:
        fps = frame_count / (curr_time - prev_time)
        frame_count = 0
        prev_time = curr_time

    cv2.putText(display_frame, f"FPS: {fps:.1f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 显示窗口
    cv2.imshow('YOLOv8 Seg - Real-time Inference', display_frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
print("👋 程序已退出")