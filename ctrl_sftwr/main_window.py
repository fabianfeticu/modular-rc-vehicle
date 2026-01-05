"""
RC Car GUI - Main Application Entry Point
"""
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QDial, 
                             QToolBar, QAction, QMenu)


from windows.motor_control import MotorControl
from windows.servo_control import ServoControl
from windows.ultrasonic_control import UltrasonicControl
from windows.sensors_control import SensorsControl
from windows.log_window import LogWindow
from windows.settings_window import SettingsWindow
from windows.test_window import test_window
from windows.light_control import LightControl


from utils.styles import apply_dark_theme


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.setWindowTitle("RC Car Control Station")
        self.resize(1000, 600)
        
        # Test label (instead of label put the servos here)
        self.test = QLabel("Test", self)
        self.test.setStyleSheet("background-color: lightgreen;")
        self.test.setFixedSize(100, 30)
        self.test.setGeometry(100, 100, 75, 55)
        """
        add sliders for each servo, position them horizontally 
        also add a master slider to control all servos at once
        """
        
        # Motor traction control add bridge to change current polarity for the motor
        self.widget = QDial(self)
        self.widget.setRange(-100, 100)
        self.widget.setSingleStep(1)
        self.widget.setGeometry(700, 100, 100, 100)

        self.widget.valueChanged.connect(self.value_changed)
        
        
        self.toolbar = QToolBar("My main toolbar")
        self.addToolBar(self.toolbar)

        
        CarOverview = QAction("Motor Control", self)
        ServoOverview = QAction("Servo Control", self)
        UltrasonicOverview = QAction("Ultrasonic Overview", self)
        LightControlBtn = QAction("Light Control", self)
        SensorsOverview = QAction("Sensors Overview", self)
        Settings = QAction("Settings", self)
        test = QAction("Test", self)
        

        # Connect actions
        CarOverview.triggered.connect(self.show_motor_control)
        ServoOverview.triggered.connect(self.show_servo_control)
        UltrasonicOverview.triggered.connect(self.show_ultrasonic_control)
        SensorsOverview.triggered.connect(self.show_sensors_control)
        Settings.triggered.connect(self.show_settings)
        test.triggered.connect(self.show_test)
        LightControlBtn.triggered.connect(self.show_light_control)

        
        self.toolbar.addAction(CarOverview)
        self.toolbar.addAction(ServoOverview)
        self.toolbar.addAction(UltrasonicOverview)
        self.toolbar.addAction(SensorsOverview)
        self.toolbar.addAction(LightControlBtn)
        self.toolbar.addAction(Settings)
        self.toolbar.addAction(test)
        

    def contextMenuEvent(self, e):
        context = QMenu(self)
        e_stop = QAction("Emergency Stop", self)
        log = QAction("Log", self)
        settings = QAction("Settings", self)

        e_stop.triggered.connect(self.emergency_stop)
        log.triggered.connect(self.logw)
        settings.triggered.connect(self.show_settings)

        context.addAction(e_stop) 
        context.addAction(log)
        context.addAction(settings)  
        context.exec(e.globalPos())

    def emergency_stop(self):  
        self.e_stop_window = MotorControl()
        self.e_stop_window.show()

    def logw(self):
        self.log_window = LogWindow()
        self.log_window.show()

    def show_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

    def show_motor_control(self):
        self.motor_control = MotorControl()
        self.motor_control.show()
    
    def show_servo_control(self):
        self.servo_control = ServoControl()
        self.servo_control.show()

    def show_ultrasonic_control(self):
        self.ultrasonic_control = UltrasonicControl()
        self.ultrasonic_control.show()

    def show_sensors_control(self):
        self.sensors_control = SensorsControl()
        self.sensors_control.show()

    def show_test(self):
        self.test_window = test_window()
        self.test_window.show()

    def show_light_control(self):
        self.light_control = LightControl()
        self.light_control.show()

    def value_changed(self, i):
        print(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    
    apply_dark_theme(app)
    
   
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
