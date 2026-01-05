"""
Sensors Control Window for RC Car GUI
Manages various sensor displays and controls
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow


class SensorsControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensors Control")
        self.setFixedSize(QSize(750, 500))
