"""
Ultrasonic Control Window for RC Car GUI
Manages ultrasonic sensor display and controls
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow


class UltrasonicControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultrasonic Control")
        self.setFixedSize(QSize(1000, 500))
