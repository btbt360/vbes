# clip_editor.py
import wave
import pyaudio
from moviepy.editor import AudioFileClip
from typing import List, Union

class AudioClipEditor:
    """基于PyAudio和MoviePy的音频剪辑工具"""
    
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=16000):
        """
        :param format: 音频格式（默认16位整型）
        :param channels: 声道数（默认单声道）
        :param rate: 采样率（默认16kHz）
        """
        self.p = pyaudio.PyAudio()
        self.format = format
        self.channels = channels
        self.rate = rate

    def record_clip(self, duration: float, output_path: str) -> None:
        """录制音频片段
        
        :param duration: 录制时长（秒）
        :param output_path: 输出文件路径
        """
        frames = []
        stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=1024
        )

        try:
            for _ in range(0, int(self.rate / 1024 * duration)):
                frames.append(stream.read(1024))
        finally:
            stream.stop_stream()
            stream.close()

        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))

    @staticmethod
    def merge_clips(file_paths: List[str], output_path: str) -> None:
        """合并多个音频文件
        
        :param file_paths: 待合并文件路径列表
        :param output_path: 合并后文件路径
        """
        clips = [AudioFileClip(f) for f in file_paths]
        final_clip = clips[0]
        for clip in clips[1:]:
            final_clip = final_clip.append(clip, crossfade=0)
        final_clip.write_audiofile(output_path)
        final_clip.close()

    def __del__(self):
        self.p.terminate()