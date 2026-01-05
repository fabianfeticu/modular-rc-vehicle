"""
Settings Window for RC Car GUI
Application settings and configuration
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(QSize(1000, 500))
