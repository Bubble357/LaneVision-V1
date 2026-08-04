from ultralytics import YOLO
import cv2
from pathlib import Path

# 1. 加载预训练模型
model = YOLO('yolov8n-seg.pt') 

# 2. 指定输入图片
# 可以直接使用数据集里的图片，或者你刚才输出的 day2_output.jpg
img_path = Path.home() / 'datasets' / 'coco8-seg' / 'images' / 'train' / '000000000030.jpg'

# 3. 运行推理
results = model(img_path)  

# 4. 可视化并保存
annotated_img = results[0].plot()  

# 5. 保存结果
output_path = 'sample_yolo_prediction.jpg'
cv2.imwrite(output_path, annotated_img)
print(f"🎉 YOLO 推理完成！结果保存为：{output_path}")