
```markdown
# LaneVision-V1：基于 YOLOv8-seg 的 CPU 端实时感知系统

<p align="center">
  <img src="sample_yolo_prediction.jpg" alt="推理效果展示" width="600"/>
</p>

<p align="center">
  <a href="#-项目简介">项目简介</a> •
  <a href="#-技术栈">技术栈</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-性能表现">性能表现</a> •
  <a href="#-效果展示">效果展示</a>
</p>

---

## 📌 项目简介

**LaneVision-V1** 是一套面向自动驾驶感知场景的**轻量级目标检测与实例分割**系统。

本项目模拟了**边缘端（CPU）算力受限**的真实工业场景，通过模型轻量化与输入分辨率适配，成功在普通办公电脑上实现了 **20 FPS** 的实时推理，并完成了从数据读取、模型推理到结果保存的**完整工程闭环**。

### 🎯 核心功能
- ✅ 支持 **单张图片 / 本地视频 / 摄像头实时流** 三种输入模式
- ✅ 输出带 **检测框（Bounding Box）** 和 **分割蒙版（Instance Mask）** 的渲染结果
- ✅ 推理结果**实时预览** + **同步保存为 MP4 文件**
- ✅ 提供数据集标注可视化工具，支持 **Ground Truth** 与模型预测的对比分析

---

## 🧠 技术栈

| 工具 | 用途 |
| :--- | :--- |
| **Python 3.10** | 开发语言 |
| **PyTorch** | 深度学习框架 |
| **YOLOv8-seg (Nano)** | 目标检测 + 实例分割模型 |
| **OpenCV** | 图像处理与视频流读写 |
| **Ultralytics** | YOLO 模型部署工具链 |
| **NumPy / Matplotlib** | 数据处理与可视化辅助 |

---

## 🚀 快速开始

### 1️⃣ 克隆仓库

```bash
git clone https://github.com/Bubble357/LaneVision-V1.git
cd LaneVision-V1
```

### 2️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

> ⚠️ 首次运行时会自动下载预训练权重 `yolov8n-seg.pt`（约 **7 MB**），请保持网络畅通。

### 3️⃣ 运行推理

| 命令 | 功能 |
| :--- | :--- |
| `python infer.py` | 单张图片推理（输出带框和蒙版的图片） |
| `python video_infer.py` | 视频/摄像头实时预览（按 `q` 或 `ESC` 退出） |
| `python video_save.py` | 视频推理并自动保存为 `output_video.mp4` |
| `python visualize.py` | 数据集标注可视化（绘制绿色多边形轮廓） |

---

## 📊 性能表现

| 硬件环境 | 输入尺寸 | 推理帧率 |
| :--- | :--- | :--- |
| Intel Core i5（无独立显卡） | 320 × 320 | **~20 FPS** |
| Intel Core i5（无独立显卡） | 640 × 640 | **~8 FPS** |

> 💡 通过降低输入分辨率（640→320），在 CPU 环境下实现了 **2.5 倍** 的推理速度提升。

---

## 📷 效果展示

| Ground Truth（人工标注） | YOLOv8-seg 预测结果 |
| :---: | :---: |
| ![GT](sample_ground_truth.jpg) | ![Pred](sample_yolo_prediction.jpg) |
| 绿色轮廓线为数据集提供的多边形分割标注 | 蓝色框 + 彩色蒙版为模型输出的检测与分割结果 |

---

## 📂 项目结构

```
LaneVision-V1/
├── infer.py                 # 单张图片推理脚本
├── video_infer.py           # 视频/摄像头实时预览脚本
├── video_save.py            # 视频推理并保存为 MP4
├── visualize.py             # 数据集标注可视化脚本
├── requirements.txt         # Python 依赖清单
├── .gitignore               # Git 忽略规则
├── sample_ground_truth.jpg  # 真值示例图
├── sample_yolo_prediction.jpg # 模型预测示例图
└── README.md                # 项目说明文档
```

---

## 💡 优化策略（工程亮点）

1. **模型轻量化**：选用 YOLOv8-seg Nano 版本，参数量仅 **3.2M**，适合边缘端部署。
2. **分辨率适配**：将输入尺寸从默认的 640×640 压缩至 320×320，计算量减少至 **1/4**。
3. **跳帧推理**：在视频流处理中支持跳帧策略，进一步平衡 CPU 负载与画面流畅度。
4. **代码与数据分离**：遵循工程规范，权重文件与数据集不纳入版本控制，通过脚本自动下载。

---

## 📅 更新日志

- **2026.08.04**：完成单图推理与视频流闭环，CPU 环境下稳定 20 FPS。
- **2026.08.03**：完成环境搭建、数据集可视化与模型部署验证。

---

## 📄 License

本项目仅供学习与展示使用。

---