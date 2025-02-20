# main.py
import yaml
from vad.detector import VADDetector
from audio_processor import AudioStream

def main():
    # 加载配置文件
    with open("config/settings.yaml") as f:
        config = yaml.safe_load(f)
    
    # 初始化语音检测器
    detector = VADDetector(
        sample_rate=config["audio_params"]["sample_rate"],
        threshold=config["audio_params"]["vad_threshold"],
        model_path=config["model_paths"]["vad_model"]
    )
    
    # 初始化音频流
    stream = AudioStream(
        device_id=config["recording"]["input_device_id"],
        frame_length=config["audio_params"]["frame_length"]
    )
    
    try:
        print("开始语音检测...")
        while True:
            # 获取音频帧并处理
            frame = stream.get_frame()
            speech_prob = detector.process_frame(frame)
            
            # 根据阈值判断语音活动
            if speech_prob > config["audio_params"]["vad_threshold"]:
                print("检测到语音活动")
                
    except KeyboardInterrupt:
        print("\n程序终止")
        stream.close()

if __name__ == "__main__":
    main()