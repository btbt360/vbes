# ui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSignal
from .ui_main_window import Ui_MainWindow  # 假设已通过pyuic生成

class MainWindow(QMainWindow, Ui_MainWindow):
    config_requested = pyqtSignal()  # 配置请求信号
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._connect_signals()
        
    def _connect_signals(self):
        """连接界面控件信号"""
        self.actionOpen.triggered.connect(self.on_open)
        self.actionSave.triggered.connect(self.on_save)
        self.btn_config.clicked.connect(self.config_requested)
        
    def on_open(self):
        """打开文件操作"""
        path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "All Files (*)")
        if path:
            self.statusbar.showMessage(f"已打开文件：{path}")
            
    def on_save(self):
        """保存文件操作"""
        path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "All Files (*)")
        if path:
            self.statusbar.showMessage(f"已保存到：{path}")