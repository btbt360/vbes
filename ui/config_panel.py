# ui/config_panel.py 
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal

class ConfigPanel(QDialog):
    config_changed = pyqtSignal(dict)  # 配置变更信号
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        
    def _setup_ui(self):
        """构建配置界面"""
        self.setWindowTitle("系统配置")
        layout = QVBoxLayout()
        
        self.input_server = QLineEdit("localhost:8080")
        self.btn_confirm = QPushButton("应用配置")
        
        layout.addWidget(self.input_server)
        layout.addWidget(self.btn_confirm)
        self.setLayout(layout)
        
        self.btn_confirm.clicked.connect(self._on_confirm)
        
    def _on_confirm(self):
        """处理配置确认事件"""
        config = {"server": self.input_server.text()}
        self.config_changed.emit(config)
        self.close()