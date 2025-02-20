````markdown
# VAD 语音检测系统

基于 PyTorch 实现的实时语音活动检测系统，支持噪声环境下的语音识别

## 🚀 功能特性

实时音频流处理
噪声抑制功能
可配置的检测阈值
多设备兼容支持
可视化结果输出（开发中）

## 📦 安装步骤

环境要求
Python 3.9+
PyTorch 2.0+
FFmpeg（音频处理依赖）

```bash
克隆仓库
git clone https://github.com/yourname/vad-system.git
cd vad-system

安装依赖（推荐使用虚拟环境）
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows

pip install -r requirements.txt
```
````

## ⚙️ 配置说明

修改`config/settings.yaml`：

```yaml
audio_params:
  sample_rate: 16000 # 采样率
  vad_threshold: 0.7 # 语音检测阈值
model_paths:
  vad_model: models/vad_model.pth
```

## 🖥️ 使用示例

```bash
python main.py --config config/settings.yaml
```

## 📂 项目结构

```
VBES/
├── audio_processor/        # 核心处理模块
│   ├── vad_detector.py     # VAD检测器
│   ├── clip_editor.py      # 音频剪辑器
│   └── __init__.py
├── ui/                     # 界面层模块
│   ├── main_window.py      # 主窗口
│   ├── config_panel.py     # 配置面板
│   └── __init__.py
├── utils/                  # 工具模块
│   ├── waveform_plotter.py # 波形绘制工具
│   └── __init__.py
├── config/                 # 配置文件
│   └── settings.yaml
├── tests/                  # 测试目录
│   └── test_vad_detector.py
├── requirements.txt        # 依赖文件
├── main.py                 # 入口脚本
└── README.md               # 文档
```

## 📄 许可证

本项目采用 MIT License (LICENSE)
