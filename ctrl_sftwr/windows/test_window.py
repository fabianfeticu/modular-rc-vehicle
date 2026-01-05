from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QSize


class test_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Window")
        self.setFixedSize(QSize(1250, 750))
        
