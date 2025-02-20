# audio_processor/vad_detector.py
import webrtcvad
from typing import Union, Tuple

class VADDetector:
    """基于WebRTC的语音活动检测器（支持呼吸声检测）
    
    特性：
    - 支持多采样率（16k/32k/48kHz）
    - 可调节检测灵敏度
    - 自动帧长度校验
    """
    
    SUPPORTED_RATES = {16000, 32000, 48000}
    VALID_FRAME_MS = (10, 20, 30)  # WebRTC VAD规范要求[9]

    def __init__(self, aggressiveness: int = 3):
        """
        :param aggressiveness: 检测灵敏度（0-3，3为最严格）
        """
        self._validate_aggressiveness(aggressiveness)
        
        self.vad = webrtcvad.Vad()
        self.vad.set_mode(aggressiveness)
        self.current_config = {
            'aggressiveness': aggressiveness,
            'sample_rate': None
        }

    def detect(self, 
              audio_frame: bytes, 
              sample_rate: int = 16000) -> bool:
        """检测音频帧是否包含语音/呼吸声
        
        :param audio_frame: PCM16单声道音频数据
        :param sample_rate: 采样率（需符合WebRTC规范）
        :return: 是否检测到有效声音
        """
        self._validate_sample_rate(sample_rate)
        self._validate_frame_length(audio_frame, sample_rate)
        
        return self.vad.is_speech(audio_frame, sample_rate)

    def _validate_aggressiveness(self, value: int):
        """校验灵敏度参数合法性"""
        if not 0 <= value <= 3:
            raise ValueError(f"无效灵敏度参数 {value}，应在0-3范围内")

    def _validate_sample_rate(self, rate: int):
        """校验采样率合规性"""
        if rate not in self.SUPPORTED_RATES:
            raise ValueError(
                f"不支持的采样率 {rate}Hz，支持：{self.SUPPORTED_RATES}"
            )

    def _validate_frame_length(self, frame: bytes, sample_rate: int):
        """校验音频帧长度符合WebRTC规范"""
        frame_ms = len(frame) // (sample_rate // 500)  # 计算帧时长(ms)
        if frame_ms not in self.VALID_FRAME_MS:
            raise ValueError(
                f"无效帧长度 {frame_ms}ms，有效值：{self.VALID_FRAME_MS}"
            )

# 示例用法（符合[4]的测试建议）
if __name__ == "__main__":
    detector = VADDetector(aggressiveness=2)
    test_frame = b'\x00' * 320  # 10ms@16kHz
    
    try:
        print(detector.detect(test_frame, 16000))
    except ValueError as e:
        print(f"参数错误：{str(e)}")