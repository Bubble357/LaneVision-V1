import cv2
from ultralytics import YOLO
import time

# 1. 加载模型
model = YOLO('yolov8n-seg.pt')

# 2. 视频输入（优先读取文件，如果没有则打开摄像头）
video_path = 'test_video.mp4'  
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("⚠️ 未找到视频文件，尝试打开摄像头...")
    cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 无法打开视频或摄像头")
    exit()

# 3. 获取视频属性（用于设置保存参数）
fps_in = cap.get(cv2.CAP_PROP_FPS)          # 原视频帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"📹 输入视频尺寸：{width}x{height}，帧率：{fps_in}")

# 4. 定义视频编码器并创建 VideoWriter 对象
# 保存为 output_video.mp4（使用 mp4v 编码，兼容性好）
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps_in, (width, height))

print("✅ 开始处理，按 'q' 退出。处理后的视频将保存为 output_video.mp4")

frame_count = 0
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("📹 视频播放完毕或读取失败")
        break

    frame_count += 1

    # 推理（为了速度，用 320 分辨率）
    resized_frame = cv2.resize(frame, (320, 320))
    results = model(resized_frame, imgsz=320, verbose=False)
    
    # 绘制标注（在缩小后的图上画）
    annotated_frame = results[0].plot()
    # 放大回原尺寸（以便保存和显示）
    display_frame = cv2.resize(annotated_frame, (width, height))

    # 计算并显示 FPS
    curr_time = time.time()
    if curr_time - prev_time >= 1.0:
        fps = frame_count / (curr_time - prev_time)
        frame_count = 0
        prev_time = curr_time

    cv2.putText(display_frame, f"FPS: {fps:.1f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 【核心】写入视频文件
    out.write(display_frame)

    # 显示窗口
    cv2.imshow('Saving Video... Press Q to quit', display_frame)

    key = cv2.waitKey(10) & 0xFF
    if key == ord('q') or key == ord('Q') or key == 27:
        break

# 释放资源
cap.release()
out.release()  # 必须释放，否则视频文件可能损坏
cv2.destroyAllWindows()
print("🎉 处理完成！视频已保存为 output_video.mp4")