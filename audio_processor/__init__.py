# audio_processor/__init__.py
"""
音频处理工具包
包含VAD检测、音频剪辑等核心功能
"""

from .vad_detector import VADDetector

__version__ = "1.0.0"
__all__ = ['VADDetector', 'AudioClipEditor']