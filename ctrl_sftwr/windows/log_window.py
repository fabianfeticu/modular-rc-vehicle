"""
Log Window for RC Car GUI
Displays system logs and events
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow


class LogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log")
        self.setFixedSize(QSize(1000, 500))
