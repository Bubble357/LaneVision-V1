\# LaneVision-V1：基于 YOLOv8-seg 的 CPU 端实时感知系统



\## 📌 项目简介



一套面向自动驾驶场景的\*\*轻量级目标检测与实例分割\*\*方案。在纯 CPU 环境下，通过模型轻量化与输入分辨率适配，实现 \*\*20 FPS\*\* 的实时推理。



\*\*核心功能\*\*：

\- 支持图片 / 视频 / 摄像头 三种输入模式

\- 输出带 \*\*检测框（Bounding Box）\*\* 和 \*\*分割蒙版（Instance Mask）\*\* 的渲染结果

\- 推理结果可实时预览，并同步保存为 MP4 文件



\---



\## 🧠 技术栈



| 工具 | 用途 |

| :--- | :--- |

| Python 3.10 | 开发语言 |

| PyTorch | 深度学习框架 |

| YOLOv8-seg (Nano) | 目标检测 + 实例分割模型 |

| OpenCV | 图像处理与视频流读写 |

| Ultralytics | YOLO 模型部署工具 |



\---



\## 🚀 快速开始



\### 1. 克隆仓库



```bash

git clone https://github.com/Bubble357/LaneVision-V1.git

cd LaneVision-V1

