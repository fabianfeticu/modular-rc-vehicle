"""
Motor Control Window for RC Car GUI
Manages front and rear motor control with dials, sliders, and preset buttons
"""
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QMainWindow, QDial, QPushButton, QLabel, 
                             QProgressBar, QSlider, QFrame)
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtWidgets


class MotorControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.front = 0
        self.rear = 0

        #labels and screen elements
        self.left_frame = QtWidgets.QFrame(self)
        self.left_frame.setGeometry(35, 20, 460, 460)
        self.left_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setStyleSheet("border: 1px solid grey;")

        self.right_frame = QtWidgets.QFrame(self)
        self.right_frame.setGeometry(510, 20, 460, 460)
        self.right_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setStyleSheet("border: 1px solid grey;")

        self.setWindowTitle("Motor Control")
        self.setFixedSize(QSize(1000, 500))
        

        self.front_label = QLabel("Front", self)
        self.front_label.setGeometry(90, 20, 100, 20)
        self.front_label.setAlignment(Qt.AlignCenter)
        self.front_label.setStyleSheet("border: 1px solid grey;")

        self.rear_label = QLabel("Rear", self)
        self.rear_label.setGeometry(325, 20, 100, 20)
        self.rear_label.setAlignment(Qt.AlignCenter)
        self.rear_label.setStyleSheet("border: 1px solid grey;")

        self.Title = QLabel("Motor Control", self)
        self.Title.setGeometry(202, 20, 110, 20)
        self.Title.setStyleSheet("border: 1px solid grey;")

        self.front_value_label = QLabel("0", self)
        self.front_value_label.setGeometry(90, 60, 100, 20)
        self.front_value_label.setAlignment(Qt.AlignCenter)
        self.front_value_label.setStyleSheet("border: 1px solid grey;")

        self.rear_value_label = QLabel("0", self)
        self.rear_value_label.setGeometry(325, 60, 100, 20)
        self.rear_value_label.setAlignment(Qt.AlignCenter)
        self.rear_value_label.setStyleSheet("border: 1px solid grey;")

        self.master_value_label = QLabel("             m/s", self)
        self.master_value_label.setGeometry(202, 60, 110, 20)
        self.master_value_label.setAlignment(Qt.AlignCenter)
        self.master_value_label.setStyleSheet("border: 1px solid grey;")


        #dials and the coresponding neutral buttons
        self.motor_front = QDial(self)
        self.motor_front.setRange(-100, 100)
        self.motor_front.setSingleStep(1)
        self.motor_front.setGeometry(90, 280, 100, 100)
        self.motor_front.valueChanged.connect(self.front_motor_dial_function)

        self.neutral_front_btn = QPushButton("Neutral", self)
        self.neutral_front_btn.setGeometry(90, 380, 100, 30)
        self.neutral_front_btn.clicked.connect(self.neutral_front)


        self.motor_rear = QDial(self)
        self.motor_rear.setRange(-100, 100)
        self.motor_rear.setSingleStep(1)
        self.motor_rear.setGeometry(325, 280, 100, 100)
        self.motor_rear.valueChanged.connect(self.rear_motor_dial_function)

        self.neutral_rear_btn = QPushButton("Neutral", self)
        self.neutral_rear_btn.setGeometry(325, 380, 100, 30)
        self.neutral_rear_btn.clicked.connect(self.neutralrear)



        #master slider
        self.masterslider = QSlider(Qt.Horizontal, self)
        self.masterslider.setRange(-100, 100)
        self.masterslider.setSingleStep(1)
        self.masterslider.setGeometry(90, 400, 335, 100)
        self.masterslider.valueChanged.connect(self.update_motors_from_master_slider)



        #neutral master btn = Stop = park break =emergency stop
        self.neutral_master_btn = QPushButton("Stop", self)
        self.neutral_master_btn.setGeometry(214,378,90,35)
        self.neutral_master_btn.setStyleSheet("QPushButton { border: 2px solid red; } QPushButton:checked { background-color: red; }")
        self.neutral_master_btn.setCheckable(True)
        self.neutral_master_btn.clicked.connect(self.neutral_master)
        
     
     
     
        # Connect dials to update bars
        self.motor_front.valueChanged.connect(self.update_bars)
        self.motor_rear.valueChanged.connect(self.update_bars)

        self.motor_front.valueChanged.connect(self.update_front)
        self.motor_rear.valueChanged.connect(self.update_rear)



        #middle buttons
        self.fwd75btn = QPushButton("75%", self)
        self.fwd75btn.setGeometry(224, 115, 70, 25)
        self.fwd75btn.setStyleSheet("background-color: darkblue;")

        self.fwd50btn = QPushButton("50%", self)
        self.fwd50btn.setGeometry(224, 150, 70, 25)
        self.fwd50btn.setStyleSheet("background-color: blue;")

        self.fwd25btn = QPushButton("25%", self)
        self.fwd25btn.setGeometry(224, 185, 70, 25)
        self.fwd25btn.setStyleSheet("background-color: #CBF6FA; color: black;")


        self.rwd75btn = QPushButton("75%", self)
        self.rwd75btn.setGeometry(224, 235, 70, 25)
        self.rwd75btn.setStyleSheet("background-color: darkred;")

        self.rwd50btn = QPushButton("50%", self)
        self.rwd50btn.setGeometry(224, 270, 70, 25)
        self.rwd50btn.setStyleSheet("background-color: red;")

        self.rwd25btn = QPushButton("25%", self)
        self.rwd25btn.setGeometry(224, 305, 70, 25)
        self.rwd25btn.setStyleSheet("background-color: pink; color: black;")

        #motor settings bars
        self.pfrontbar = QProgressBar(self)
        self.pfrontbar.setGeometry(113, 120, 25, 160)
        self.pfrontbar.setOrientation(Qt.Vertical)
        self.pfrontbar.setTextDirection(QProgressBar.TopToBottom)
        self.pfrontbar.setRange(0, 100)
        self.pfrontbar.setValue(0)
        
        self.nfrontbar = QProgressBar(self)
        self.nfrontbar.setGeometry(143, 120, 25, 160)
        self.nfrontbar.setOrientation(Qt.Vertical)
        self.nfrontbar.setTextDirection(QProgressBar.TopToBottom)
        self.nfrontbar.setRange(0, 100)
        self.nfrontbar.setValue(0)
        palette = self.nfrontbar.palette()
        palette.setColor(QPalette.Highlight, Qt.red)
        self.nfrontbar.setPalette(palette)
        self.nfrontbar.setTextVisible(False)

       
        self.prearbar = QProgressBar(self)
        self.prearbar.setGeometry(347, 120, 25, 160)
        self.prearbar.setOrientation(Qt.Vertical)
        self.prearbar.setTextDirection(QProgressBar.TopToBottom)
        self.prearbar.setRange(0, 100)
        self.prearbar.setValue(0)
        
        self.nrearbar = QProgressBar(self)
        self.nrearbar.setGeometry(377, 120, 25, 160)
        self.nrearbar.setOrientation(Qt.Vertical)
        self.nrearbar.setTextDirection(QProgressBar.TopToBottom)
        self.nrearbar.setRange(0, 100)
        self.nrearbar.setValue(0)
        palette = self.nrearbar.palette()
        palette.setColor(QPalette.Highlight, Qt.red)
        self.nrearbar.setPalette(palette)
        self.nrearbar.setTextVisible(False)



        #right frame cruise control buttons
        #row1
        self.forward_mode_btn = QPushButton("+10%", self)
        self.forward_mode_btn.setGeometry(560, 338, 100, 30)
        self.forward_mode_btn.setStyleSheet("background-color: darkblue;")
        self.forward_mode_btn.clicked.connect(lambda: self.masterslider.setValue(self.masterslider.value() + 10))

        self.eco_mode_btn = QPushButton("Drift", self)
        self.eco_mode_btn.setGeometry(695, 338, 100, 30)
        self.eco_mode_btn.setStyleSheet("background-color: Purple; color: white")
        self.eco_mode_btn.pressed.connect(self.action_eco_pressed)
        self.eco_mode_btn.released.connect(self.action_eco_released)

        self.rearward_mode_btn = QPushButton("-10%", self)
        self.rearward_mode_btn.setGeometry(830, 338, 100, 30)
        self.rearward_mode_btn.setStyleSheet("background-color: #6495ED;")
        self.rearward_mode_btn.clicked.connect(lambda: self.masterslider.setValue(self.masterslider.value() - 10))
        
        # Control buttons under speedometer
        self.control_mode_btn = QPushButton("FWD Ctrl", self.right_frame)
        self.control_mode_btn.setGeometry(218, 95, 90, 30)
        self.control_mode_btn.setStyleSheet("background-color: blue; color: white")
        self.control_mode_btn.pressed.connect(self.action_control_pressed)
        self.control_mode_btn.released.connect(self.action_control_released)

        self.reverse_control_btn = QPushButton("REV Ctrl", self.right_frame)
        self.reverse_control_btn.setGeometry(318, 95, 90, 30)
        self.reverse_control_btn.setStyleSheet("background-color: red; color: black")
        self.reverse_control_btn.pressed.connect(self.action_reverse_control_pressed)
        self.reverse_control_btn.released.connect(self.action_reverse_control_released)
        
        
        #row2
        self.maxthr_btn = QPushButton("Max Thr", self)
        self.maxthr_btn.setGeometry(560, 378, 100, 30)
        self.maxthr_btn.setStyleSheet("background-color: darkblue;")
        
        self.cruise_btn = QPushButton("Cruise", self)
        self.cruise_btn.setGeometry(695, 378, 100, 30)
        self.cruise_btn.setStyleSheet("background-color: darkgreen;")

        self.minthr_btn = QPushButton("Max Rev Thr", self)
        self.minthr_btn.setGeometry(830, 378, 100, 30)
        self.minthr_btn.setStyleSheet("background-color: darkred;")
        

       
        #row3
        self.fwd_btn = QPushButton("FWD",self)
        self.fwd_btn.setGeometry(560, 420, 100, 30)
        self.fwd_btn.setStyleSheet("background-color: gold; color: black")
        
        self.awd_btn = QPushButton("Neutral",self)
        self.awd_btn.setGeometry(695, 420, 100, 30)
        self.awd_btn.setStyleSheet("background-color: silver")
        self.awd_btn.clicked.connect(self.action_awd)
        
        self.rwd_btn = QPushButton("RWD",self)
        self.rwd_btn.setGeometry(830, 420, 100, 30)
        self.rwd_btn.setStyleSheet("background-color: purple;")

        # Connect Buttons
        self.fwd75btn.clicked.connect(self.set_speed_fwd_75)
        self.fwd50btn.clicked.connect(self.set_speed_fwd_50)
        self.fwd25btn.clicked.connect(self.set_speed_fwd_25)
        
        self.rwd75btn.clicked.connect(self.set_speed_rwd_75)
        self.rwd50btn.clicked.connect(self.set_speed_rwd_50)
        self.rwd25btn.clicked.connect(self.set_speed_rwd_25)
        
        
        self.maxthr_btn.clicked.connect(self.set_max_thr)
        self.minthr_btn.clicked.connect(self.set_min_thr)
        self.cruise_btn.clicked.connect(self.action_cruise)
        
        self.fwd_btn.clicked.connect(self.action_fwd)
        self.awd_btn.clicked.connect(self.action_awd)
        self.rwd_btn.clicked.connect(self.action_rwd)




        #esthetics 
        self.container_frames = QFrame(self.right_frame)
        self.container_frames.setGeometry(50, 40, 140, 220)
        self.container_frames.setFrameShape(QFrame.StyledPanel)
        self.container_frames.setFrameShadow(QFrame.Raised)

        self.frame1 = QFrame(self.container_frames)
        self.frame1.setGeometry(5, 5, 30, 50)
        self.frame1.setFrameShape(QFrame.Box)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.frame1.setStyleSheet("border: 1px solid grey; background-color: grey;")

        #esthetics 
        self.frame_middle = QFrame(self.container_frames)
        self.frame_middle.setGeometry(70, 5, 1, 210)
        self.frame_middle.setFrameShape(QFrame.Box)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.frame_middle.setStyleSheet("border: 1px solid grey; background-color: grey;")

        #esthetics 

        self.line_top = QFrame(self.container_frames)
        self.line_top.setGeometry(35, 30, 70, 1)
        self.line_top.setStyleSheet("background-color: grey;")

        self.line_bottom = QFrame(self.container_frames)
        self.line_bottom.setGeometry(35, 190, 70, 1)
        self.line_bottom.setStyleSheet("background-color: grey;")

        
        self.frame2 = QFrame(self.container_frames)
        self.frame2.setGeometry(105, 5, 30, 50)
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.setStyleSheet("border: 1px solid grey; background-color: grey;")

        self.frame3 = QFrame(self.container_frames)
        self.frame3.setGeometry(5, 165, 30, 50)
        self.frame3.setFrameShape(QFrame.Box)
        self.frame3.setFrameShadow(QFrame.Raised)
        self.frame3.setStyleSheet("border: 1px solid grey; background-color: grey;")

        self.frame4 = QFrame(self.container_frames)
        self.frame4.setGeometry(105, 165, 30, 50)
        self.frame4.setFrameShape(QFrame.Box)
        self.frame4.setFrameShadow(QFrame.Raised)
        self.frame4.setStyleSheet("border: 1px solid grey; background-color: grey;")
        

        self.label_speed = QLabel("Speed: 0 m/s", self.right_frame)
        self.label_speed.setGeometry(250, 45, 125, 30)
        self.label_speed.setStyleSheet("border: 1px solid grey; color:grey")

        
    

    
    """
    FUNCTIONS  
    """ 
    def update_front(self, value):
        self.front = value
    
    def update_rear(self,value):
        self.rear = value


    def set_speed(self, value):
        self.label_speed.setText("Speed: "+str(value)+" m/s")   #connect to arduino gps module

    #while in stop mode the buttons are disabled
    def neutral_master(self):
        
        if self.neutral_master_btn.isChecked():
            self.masterslider.setValue(0)
            self.motor_front.setValue(0)
            self.motor_rear.setValue(0)
            self.front = 0
            self.rear = 0
            print("STOP FUNCTION ACTIVE\\nfront: 0 , rear: 0")
            
            self.pfrontbar.setValue(0)
            self.nfrontbar.setValue(0)
            self.prearbar.setValue(0)
            self.nrearbar.setValue(0)
            
            
            
              
            self.masterslider.setEnabled(False)
            self.motor_front.setEnabled(False)
            self.motor_rear.setEnabled(False)
            self.neutral_front_btn.setEnabled(False)
            self.neutral_rear_btn.setEnabled(False)
            self.forward_mode_btn.setEnabled(False)
            self.control_mode_btn.setEnabled(False)
            self.eco_mode_btn.setEnabled(False)
            self.reverse_control_btn.setEnabled(False)
            self.rearward_mode_btn.setEnabled(False)
            self.maxthr_btn.setEnabled(False)
            self.minthr_btn.setEnabled(False)
            self.cruise_btn.setEnabled(False)
            self.fwd_btn.setEnabled(False)
            self.awd_btn.setEnabled(False)
            self.rwd_btn.setEnabled(False)
            self.forward_mode_btn.setEnabled(False)
            self.control_mode_btn.setEnabled(False)
            self.eco_mode_btn.setEnabled(False)
            self.reverse_control_btn.setEnabled(False)
            self.rearward_mode_btn.setEnabled(False)
            self.maxthr_btn.setEnabled(False)
            self.minthr_btn.setEnabled(False)
            self.cruise_btn.setEnabled(False)
            self.fwd_btn.setEnabled(False)
            self.awd_btn.setEnabled(False)
            self.rwd_btn.setEnabled(False)
            self.fwd75btn.setEnabled(False)
            self.fwd50btn.setEnabled(False)
            self.fwd25btn.setEnabled(False)
            self.rwd75btn.setEnabled(False)
            self.rwd50btn.setEnabled(False)
            self.rwd25btn.setEnabled(False)
        else:
            self.masterslider.setEnabled(True)
            self.motor_front.setEnabled(True)
            self.motor_rear.setEnabled(True)
            self.neutral_front_btn.setEnabled(True)
            self.neutral_rear_btn.setEnabled(True)
            self.forward_mode_btn.setEnabled(True)
            self.control_mode_btn.setEnabled(True)
            self.eco_mode_btn.setEnabled(True)
            self.reverse_control_btn.setEnabled(True)
            self.rearward_mode_btn.setEnabled(True)
            self.maxthr_btn.setEnabled(True)
            self.minthr_btn.setEnabled(True)
            self.cruise_btn.setEnabled(True)
            self.fwd_btn.setEnabled(True)
            self.awd_btn.setEnabled(True)
            self.rwd_btn.setEnabled(True)
            self.fwd75btn.setEnabled(True)
            self.fwd50btn.setEnabled(True)
            self.fwd25btn.setEnabled(True)
            self.rwd75btn.setEnabled(True)
            self.rwd50btn.setEnabled(True)
            self.rwd25btn.setEnabled(True)
            print("STOP FUNCTION DEACTIVATED\\nvehicle ready to start")

    def update_motors_from_master_slider(self, value):
        self.motor_front.setValue(value)
        self.motor_rear.setValue(value)

    def update_bars(self):
        
        val_f = self.motor_front.value()
        if val_f > 0:
            self.pfrontbar.setValue(val_f)
            self.nfrontbar.setValue(0)
            self.front=int(val_f)
            self.frame1.setStyleSheet("border: 1px solid grey; background-color: darkblue;")
            self.frame2.setStyleSheet("border: 1px solid grey; background-color: darkblue;")
            self.front_value_label.setStyleSheet("border: 1px solid blue;")
        else:
            self.pfrontbar.setValue(0)
            self.nfrontbar.setValue(abs(val_f))
            self.front=int(val_f)
            if val_f < 0:
                self.frame1.setStyleSheet("border: 1px solid grey; background-color: red;")
                self.frame2.setStyleSheet("border: 1px solid grey; background-color: red;")
                self.front_value_label.setStyleSheet("border: 1px solid red;")
            else:
                self.frame1.setStyleSheet("border: 1px solid grey; background-color: grey;")
                self.frame2.setStyleSheet("border: 1px solid grey; background-color: grey;")
                self.front_value_label.setStyleSheet("border: 1px solid grey;")

       
        val_r = self.motor_rear.value()
        if val_r > 0:
            self.prearbar.setValue(val_r)
            self.nrearbar.setValue(0)
            self.rear=int(val_r)
            self.frame3.setStyleSheet("border: 1px solid grey; background-color: darkblue;")
            self.frame4.setStyleSheet("border: 1px solid grey; background-color: darkblue;")
            self.rear_value_label.setStyleSheet("border: 1px solid blue")
        else:
            self.prearbar.setValue(0)
            self.nrearbar.setValue(abs(val_r))
            self.rear=int(val_r)
            
            if val_r < 0:
                self.frame3.setStyleSheet("border: 1px solid grey; background-color: red;")
                self.frame4.setStyleSheet("border: 1px solid grey; background-color: red;")
                self.rear_value_label.setStyleSheet("border: 1px solid red")
            else:
                self.frame3.setStyleSheet("border: 1px solid grey; background-color: grey;")
                self.frame4.setStyleSheet("border: 1px solid grey; background-color: grey;")
                self.rear_value_label.setStyleSheet("border: 1px solid grey")

    def update_labels(self):
        # Update Front Label
        if self.front > 0:
            self.front_value_label.setText(f"+{self.front}")
        elif self.front < 0:
            self.front_value_label.setText(f"{self.front}")
        else:
            self.front_value_label.setText("0")

        # Update Rear Label
        if self.rear > 0:
            self.rear_value_label.setText(f"+{self.rear}")
        elif self.rear < 0:
            self.rear_value_label.setText(f"{self.rear}")
        else:
            self.rear_value_label.setText("0")

    def neutral_front(self):
        self.motor_front.setValue(0)
        self.front = 0
        self.front=int(self.front)
        self.update_labels()
        print("set front: "+str(self.front))
    
    def neutralrear(self):
        self.motor_rear.setValue(0)
        self.rear = 0
        self.rear = int(self.rear)
        self.update_labels()
        print("set rear: "+str(self.rear))
    
    def front_motor_dial_function(self,value):
        self.front=int(value)
        self.update_labels()
        print("set front: "+str(self.front))
    
    def rear_motor_dial_function(self,value):
        self.rear=int(value)
        self.update_labels()
        print("set rear: "+str(self.rear))
    
       

    # Button Action Functions
    def set_speed_fwd_75(self):
        self.masterslider.setValue(75)
        
    def set_speed_fwd_50(self):
        self.masterslider.setValue(50)
        
    def set_speed_fwd_25(self):
        self.masterslider.setValue(25)
        
    def set_speed_rwd_75(self):
        self.masterslider.setValue(-75)
        
    def set_speed_rwd_50(self):
        self.masterslider.setValue(-50)
        
    def set_speed_rwd_25(self):
        self.masterslider.setValue(-25)

    def set_mode_forward(self):
        self.masterslider.setValue(50)

    def set_mode_neutral(self):
        self.masterslider.setValue(0)

    def set_mode_rearward(self):
        self.masterslider.setValue(-50)

    def set_max_thr(self):
        self.masterslider.setValue(100)

    def set_min_thr(self):
        self.masterslider.setValue(-100)

    def action_cruise(self):
        self.masterslider.setValue(35)#change to whatever power is needed to keep same speed

    def action_fwd(self):
        self.motor_rear.setValue(0)
        if self.motor_front.value() == 0:
            self.motor_front.setValue(35)
        else:
            pass

    def action_awd(self):
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
        self.masterslider.setValue(0)

    def action_rwd(self):
        self.motor_front.setValue(0)
        if self.motor_rear.value() == 0:
            self.motor_rear.setValue(35)
        else:
            pass

    def action_control_pressed(self):
        self.control_mode_btn.setStyleSheet("background-color: darkblue;")
        self.control_mode_btn.setText("Release")   
        self.motor_front.setValue(50)
        self.motor_rear.setValue(50)
        self.masterslider.setValue(50)
        
    def action_control_released(self):
        self.control_mode_btn.setStyleSheet("background-color: blue; color: white")
        self.control_mode_btn.setText("FWD Ctrl")   
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
        self.masterslider.setValue(0)
        
    def action_reverse_control_pressed(self):
        self.reverse_control_btn.setStyleSheet("background-color: darkred; color: white")
        self.reverse_control_btn.setText("Release")   
        self.motor_front.setValue(-50)
        self.motor_rear.setValue(-50)
        self.masterslider.setValue(-50)
        
    def action_reverse_control_released(self):
        self.reverse_control_btn.setStyleSheet("background-color: red; color: black")
        self.reverse_control_btn.setText("REV Ctrl")   
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
        self.masterslider.setValue(0)
    
    def action_eco_pressed(self):
        
        self.motor_front.setValue(100)
        self.motor_rear.setValue(-30)  
        self.eco_mode_btn.setStyleSheet("background-color: darkpurple; color: white")
        self.eco_mode_btn.setText("Release")


    def action_eco_released(self):
        
        self.eco_mode_btn.setStyleSheet("background-color: Purple; color: white")
        self.eco_mode_btn.setText("Drift")
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
        self.motor_front.setValue(50)
        self.motor_rear.setValue(50)
        self.masterslider.setValue(50)
        
    def action_control_released(self):
        self.control_mode_btn.setStyleSheet("background-color: blue; color: white")
        self.control_mode_btn.setText("FWD Ctrl")   
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
        self.masterslider.setValue(0)
        
    def action_reverse_control_pressed(self):
        self.reverse_control_btn.setStyleSheet("background-color: darkred; color: white")
        self.reverse_control_btn.setText("Release")   
        self.motor_front.setValue(-50)
        self.motor_rear.setValue(-50)
        self.masterslider.setValue(-50)
        
    def action_reverse_control_released(self):
        self.reverse_control_btn.setStyleSheet("background-color: red; color: black")
        self.reverse_control_btn.setText("REV Ctrl")   
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
        self.masterslider.setValue(0)
    
    def action_eco_pressed(self):
        
        self.motor_front.setValue(100)
        self.motor_rear.setValue(-30)  
        self.eco_mode_btn.setStyleSheet("background-color: darkpurple; color: white")
        self.eco_mode_btn.setText("Release")


    def action_eco_released(self):
        
        self.eco_mode_btn.setStyleSheet("background-color: Purple; color: white")
        self.eco_mode_btn.setText("Drift")
        self.motor_front.setValue(0)
        self.motor_rear.setValue(0)
