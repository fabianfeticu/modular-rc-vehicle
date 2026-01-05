"""
Servo Control Window for RC Car GUI
Manages servo controls for steering
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class ServoControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Servo Control")
        self.setFixedSize(QSize(850, 500))

        # Left frame
        self.left_frame_servo = QtWidgets.QFrame(self)
        self.left_frame_servo.setGeometry(20, 20, 395, 460) 
        self.left_frame_servo.setFrameShape(QtWidgets.QFrame.Box)
        self.left_frame_servo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame_servo.setStyleSheet("border: 1px solid grey;")

        # Right frame
        self.right_frame_servo = QtWidgets.QFrame(self)
        self.right_frame_servo.setGeometry(435, 20, 395, 460) 
        self.right_frame_servo.setFrameShape(QtWidgets.QFrame.Box)
        self.right_frame_servo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame_servo.setStyleSheet("border: 1px solid grey;")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw in upper-left quarter of left frame
        # Left frame is at (20, 20) with size (395, 460)
        # Quarter would be roughly 1/4 of the width and height
        x = 30  # 20 (frame x) + 10 (padding)
        y = 30  # 20 (frame y) + 10 (padding)
        width = 100
        height = 80
        
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.setBrush(QBrush(Qt.GlobalColor.white))
        painter.drawRect(x, y, width, height)
        painter.end()
