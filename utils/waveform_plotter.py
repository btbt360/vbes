# utils/waveform_plotter.py
import matplotlib
matplotlib.use('Qt5Agg')  # 设置Qt后端
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class WaveformPlotter(FigureCanvas):
    """实时波形绘制组件"""
    
    def __init__(self, parent=None, width=8, height=4, dpi=100):
        # 创建图形和坐标轴
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        super().__init__(self.fig)
        self.setParent(parent)
        
        # 初始化空白波形
        self._init_plot()
    
    def _init_plot(self):
        """初始化绘图区域"""
        self.axes.set_title("实时波形")
        self.axes.set_xlabel("时间")
        self.axes.set_ylabel("振幅")
        self.line, = self.axes.plot([], [])
        self.fig.tight_layout()
    
    def update_waveform(self, data):
        """更新波形数据
        Args:
            data: 新波形数据(numpy数组)
        """
        x = np.arange(len(data))
        self.line.set_data(x, data)
        self.axes.relim()
        self.axes.autoscale_view()
        self.draw()