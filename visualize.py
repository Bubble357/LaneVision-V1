import cv2
import numpy as np
from pathlib import Path

# 自动定位数据集
dataset_path = Path.home() / 'datasets' / 'coco8-seg'
img_path = dataset_path / 'images' / 'train' / '000000000030.jpg'
label_path = dataset_path / 'labels' / 'train' / '000000000030.txt'

# 检查文件
if not img_path.exists():
    print(f"❌ 图片不存在: {img_path}")
    exit()
if not label_path.exists():
    print(f"❌ 标签不存在: {label_path}")
    exit()

# 读取图片
img = cv2.imread(str(img_path))
if img is None:
    print("❌ 图片加载失败")
    exit()
h, w = img.shape[:2]
print(f"✅ 图片加载成功，尺寸：{w} x {h}")

# 画绿色多边形
with open(label_path, 'r') as f:
    lines = f.readlines()
print(f"📄 该图片中有 {len(lines)} 个标注物体")

for line in lines:
    parts = list(map(float, line.strip().split()))
    points = parts[1:]
    pts = []
    for i in range(0, len(points), 2):
        px = int(points[i] * w)
        py = int(points[i+1] * h)
        pts.append([px, py])
    pts = np.array(pts, dtype=np.int32)
    cv2.polylines(img, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

# 保存结果
cv2.imwrite('sample_ground_truth.jpg', img)
print(f"🎉 可视化完成！图片已保存为：sample_ground_truth.jpg")