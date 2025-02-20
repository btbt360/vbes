# tests/test_vad_detector.py
import pytest
import yaml
from vad.detector import VADDetector  # 假设已实现VAD检测器

@pytest.fixture(scope="module")
def config():
    """加载测试配置"""
    with open("config/settings.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture
def vad_instance(config):
    """创建VAD检测器实例"""
    return VADDetector(
        sample_rate=config["audio_params"]["sample_rate"],
        frame_length=config["audio_params"]["frame_length"],
        threshold=config["audio_params"]["vad_threshold"]
    )

class TestVADDetector:
    """VAD检测器测试套件"""
    
    @pytest.mark.parametrize("noise_level", [0.1, 0.3, 0.5])
    def test_silence_detection(self, vad_instance, noise_level):
        """测试静音检测功能"""
        # 生成带噪声的测试帧
        test_frame = np.random.normal(0, noise_level, vad_instance.frame_length)
        
        # 处理帧并验证结果
        result = vad_instance.process_frame(test_frame)
        if noise_level < vad_instance.threshold:
            assert result is False, "应检测为静音"
        else:
            assert result is True, "应检测为语音"

    def test_real_time_detection(self, vad_instance):
        """测试实时检测流程"""
        # 模拟连续音频流
        silent_frames = 5
        for _ in range(silent_frames):
            vad_instance.process_frame(np.zeros(vad_instance.frame_length))
        
        assert vad_instance.silent_frame_count == silent_frames, "静音帧计数错误"
        
        # 模拟语音帧触发状态切换
        speech_frame = np.random.normal(0, 0.8, vad_instance.frame_length)
        vad_instance.process_frame(speech_frame)
        assert vad_instance.silent_frame_count == 0, "应重置静音计数器"