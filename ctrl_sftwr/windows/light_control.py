import sys 
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, 
                             QVBoxLayout, QLabel, QFrame, QDial,QHBoxLayout, 
                             QComboBox, QPushButton,QPushButton, QProgressBar, QSlider)
import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.styles import apply_dark_theme


from PyQt5.QtCore import QTimer
from utils.comms import send_serial
import os

class LightControl(QMainWindow):
   

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Light Control")
        self.resize(QSize(1000, 500))

        self.leds = []

        
        self.presets = ["upleft","up","upright","left","full","right","downleft","down","downright","X","#","9","none","rightD","leftD","horz.D","vert.D"]
        
        current_dir=os.path.dirname(os.path.abspath(__file__))
        assets_path = os.path.join(current_dir, "..", "Assets")


        

        self.img_ls = {
            "0": os.path.join(assets_path, "upleft.png"),
            "1": os.path.join(assets_path, "up.png"),
            "2": os.path.join(assets_path, "upright.png"),
            "3": os.path.join(assets_path, "left.png"),
            "4": os.path.join(assets_path, "center.png"),
            "5": os.path.join(assets_path, "right.png"),
            "6": os.path.join(assets_path, "downleft.png"),
            "7": os.path.join(assets_path, "down.png"),
            "8": os.path.join(assets_path, "downright.png")
        }

        self.icons = {
            str(i): QIcon(path) for i, path in self.img_ls.items()
        }
        
        self.led_matrix_ls = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

        def send_costum_func():
            flat_list = [str(item) for row in self.led_matrix_ls for item in row]
            print(flat_list)
            self.send_serial(flat_list)

        def btn_to_matrix(btn,is_checked):
            print(btn)
            row = btn // 5
            col = btn - row*5
            if is_checked:
                self.led_matrix_ls[row][col] = 1
            else:
                 self.led_matrix_ls[row][col] = 0
            print(self.led_matrix_ls)
                 
        
      

                  

        self.patterns = {
            "up": [3, 7, 8, 9, 11, 13, 15, 18, 23],
            "down": [23, 17, 18, 19, 11, 13, 15, 8, 3],
            "left": [11, 7, 12, 17, 3, 13, 23, 14, 15],
            "right": [15, 9, 14, 19, 3, 23, 13, 12, 11],

            "upleft": [1, 2, 6, 7, 13, 19, 25, 3, 11],
            "upright": [5, 4, 10, 9, 13, 17, 21, 3, 15],
            "downleft": [21, 16, 22, 17, 13, 9, 5, 23, 11],
            "downright": [25, 24, 20, 19, 13, 7, 1, 23, 15],

            "X": [1, 7, 13, 19, 25, 5, 9, 17, 21],
            "#": [2, 4, 6, 7, 8, 9, 10, 12, 14, 16, 17, 18, 19, 20, 22, 24],
            "9": [1, 3, 5, 11, 13, 15, 21, 23, 25],
            "full": list(range(1, 26)),
            "none": [],

            "rightD":[1, 3, 5, 7, 9, 11 ,13, 15, 17, 19, 21, 23, 25],
            "leftD":[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
            "horz.D":[1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25],
            "vert.D":[1, 3, 5, 6, 8, 10, 11, 13, 15, 16, 18, 20, 21, 23, 25]


        }
        self.animations = ["snake","loading","wave","flower"]
        #
        self.active_visual = []
        #
        self.all_visuals =[]
        #stores led reds
        self.red_leds =[1,3,5,11,13,15,21,23,25]

        self.current_strobe_pattern =""

        self.Current_mm_Value = 0
        
        self.timer_on = QTimer()
        self.timer_on.timeout.connect(self.strobe_beat)


        self.strobe_state = False 
        
        def stop_time():
             self.timer_on.stop()


        

      

        def update_strobestate(argument):
            self.strobe_state=argument


        self.maincontainer = QWidget()
    

        #bigframes
        self.framesgrid = QHBoxLayout()
    
        self.frameleft = QFrame()
        self.frameleft.setFrameShape(QFrame.Box)
        self.frameleft.setFrameShadow(QFrame.Raised)
        self.frameleft.setStyleSheet("""
                QFrame { 
                    border: 1px solid #88b6db; 
                }
                QPushButton:checked {
                    border: 2px solid #88b6db;
                }
            """)

        self.frameright = QFrame()
        self.frameright.setFrameShape(QFrame.Box)
        self.frameright.setFrameShadow(QFrame.Raised)
        self.frameright.setStyleSheet("border: 1px solid grey;")

        self.framesgrid.addWidget(self.frameleft)
        self.framesgrid.addWidget(self.frameright)

        self.maincontainer.setLayout(self.framesgrid)
        self.setCentralWidget(self.maincontainer)

        #smallframes (right)
        self.graphframegrid = QVBoxLayout()

        self.gframeup = QFrame()
        self.gframeup.setFrameShape(QFrame.Box)
        self.gframeup.setFrameShadow(QFrame.Raised)
        self.gframeup.setStyleSheet("border: 1px solid grey;")

        self.gframedwn = QFrame()
        self.gframedwn.setFrameShape(QFrame.Box)
        self.gframedwn.setFrameShadow(QFrame.Raised)
        self.gframedwn.setStyleSheet("border: 1px solid grey;")

        self.graphframegrid.addWidget(self.gframeup)
        self.graphframegrid.addWidget(self.gframedwn)


        self.frameright.setLayout(self.graphframegrid)

        #preset Buttons layout
        self.preset_grid = QGridLayout()
        #layout for up right items
        self.preset_container = QHBoxLayout()
        
        self.preset_grid.setHorizontalSpacing(1)
        self.preset_grid.setVerticalSpacing(1)
        self.preset_grid.setContentsMargins(10, 10, 10, 10)

        for i in range(len(self.presets)-5):
            preset_btn = QPushButton()
            preset_btn.clicked.connect(lambda checked, val=i:(self.send_preset(val),self.set_visual(val)) and None)
            preset_btn.clicked.connect(lambda : update_strobestate(False))
            preset_btn.clicked.connect(lambda: stop_time())
        
            if i <=8:
                preset_btn.setFixedSize(80,80)
                preset_btn.setIcon(QIcon(self.img_ls[str(i)]))
                preset_btn.setIconSize(QSize(80,80))

            else:
                preset_btn.setFixedSize(80,40)
                preset_btn.setText(f'{self.presets[i]} Button')
                preset_btn.setIconSize(QSize(80,40))
            
            self.preset_grid.addWidget(preset_btn,i//3,i%3)
      
        
        
        self.preset_grid.setColumnStretch(0, 1)
        self.preset_grid.setColumnStretch(4, 1)

        
        self.gframeup.setLayout(self.preset_container)

        self.animations_layout = QVBoxLayout()
        self.animations_grid = QGridLayout()
       
        
        #animation buttons
        for i in range(4):
            anm_btn = QPushButton(f'{self.presets[i+13]}')
            anm_btn.clicked.connect(lambda _,  val=i: self.send_preset(val+13))
            anm_btn.clicked.connect(lambda : update_strobestate(False))
            anm_btn.clicked.connect(lambda: stop_time())
            anm_btn.clicked.connect(lambda _, val=i: self.set_visual(val+13))
            self.animations_grid.addWidget(anm_btn,0,i+1)
            anm_btn.setFixedSize(60,60)

        self.animations_grid.setColumnStretch(0, 1)
        self.animations_grid.setColumnStretch(4, 1)


        #preview gris up right
        self.visual_grid = QGridLayout()

        for i in range(25):
            vsl_led = QLabel()
            self.all_visuals.append(vsl_led)
            self.visual_grid.addWidget(vsl_led,i//5,i%5)
            vsl_led.setFixedSize(25,25)
            idx = i+1
            if idx in self.red_leds:
                vsl_led.setStyleSheet("background-color: red; border-radius: 12px;")
            else:
                vsl_led.setStyleSheet("background-color: yellow; border-radius: 12px;")
            


        self.visual_grid.setVerticalSpacing(15)
        self.visual_grid.setColumnStretch(1, 1)
        self.visual_grid.setColumnStretch(4, 1)


        self.animations_layout.addLayout(self.visual_grid)
        self.preset_container.addLayout(self.preset_grid)
        self.animations_layout.addLayout(self.animations_grid)
        self.preset_container.addLayout(self.animations_layout)
        
        


        self.led_matrix= QGridLayout()
        
        #led buttons
        for i in range(25):
            led_btn=QPushButton(f'Led{i+1}')
            led_btn.clicked.connect(lambda checked, val=i:btn_to_matrix(val,checked))
            led_btn.setFixedSize(60,60)
            self.leds.append(led_btn)
            self.led_matrix.addWidget(led_btn,i//5,i%5)

        for i in range(len(self.leds)):
            self.leds[i].setCheckable(True)

        


        self.frameleft.setLayout(self.led_matrix)



        self.dmenugrid = QGridLayout()#associated grid. down on the right side. menu for strobe and sending costum patterns

        self.stop_btn = QPushButton("OFF")#stop btn for stopping display
        self.stop_btn.setFixedSize(150,30)
        self.stop_btn.clicked.connect(lambda:self.set_visual_null())
        self.stop_btn.setStyleSheet("background-color: #4f4a4a; color:dark grey")

        self.selected_label = QComboBox()#label for selected preset to strobe
        self.selected_label.addItems(self.presets)
        self.selected_label.setStyleSheet("background-color: #4f4a4a;font-family: 'Segoe UI ';")
        self.selected_label.setFixedSize(150,30)

        self.mm_label = QLabel()#how many mm
        self.mm_label.setFixedSize(150,30)

        self.send_costum_btn = QPushButton("Send Custom")#send costum pattern
        self.send_costum_btn.clicked.connect(send_costum_func)
        self.send_costum_btn.setFixedSize(150,30)

        self.send_strobe_btn = QPushButton("Send Strobe")#send strobe
        self.send_strobe_btn.setFixedSize(150,30)
        self.send_strobe_btn.clicked.connect(lambda:self.send_strobe(self.mm_label.text()))
        self.send_strobe_btn.clicked.connect(lambda:self.display_strobe(self.presets.index(self.selected_label.currentText())))
        self.send_strobe_btn.clicked.connect(lambda: stop_time())
        self.send_strobe_btn.clicked.connect(lambda:self.timer_on.start(self.Current_mm_Value))
        self.send_strobe_btn.clicked.connect(lambda : update_strobestate(True))

        self.mm_slider = QSlider(Qt.Orientation.Horizontal)#slider for mm
        self.mm_slider.setFixedSize(150,30)
        self.mm_slider.setRange(1,100)
        self.mm_slider.setStyleSheet("border: none;")
        self.mm_slider.valueChanged.connect(self.update_mm)

        self.dmenugrid.addWidget(self.stop_btn,0,0)
        self.dmenugrid.addWidget(self.selected_label,0,1)
        self.dmenugrid.addWidget(self.mm_label,0,2)
        self.dmenugrid.addWidget(self.send_costum_btn,1,0)
        self.dmenugrid.addWidget(self.send_strobe_btn,1,1)
        self.dmenugrid.addWidget(self.mm_slider,1,2)

        self.gframedwn.setLayout(self.dmenugrid)
    
    def update_mm(self,value): 
            
            self.Current_mm_Value = value*10
            self.mm_label.setText(f"{self.Current_mm_Value} ms")

    def strobe_beat(self):
        idx = self.presets.index(self.selected_label.currentText())
        self.display_strobe(idx)

    def display_strobe(self,visual):
        if(self.strobe_state==False):
            return
        if self.current_strobe_pattern == 12: 
            self.current_strobe_pattern = visual
        else:
            self.current_strobe_pattern = 12 
            
        self.set_visual(self.current_strobe_pattern)

    
    def set_visual(self,item):
            self.active_visual=[]
            item_name = self.presets[item]
            pos_ls = []
            pos_ls = self.patterns[item_name] 
            self.active_visual.append(pos_ls)
            
            for i in range(1, 26): 
                if i not in pos_ls:
                    
                    if i in self.red_leds:
                        self.all_visuals[i-1].setStyleSheet("background-color: #8E5A5A; border-radius: 12px;")
                    else:
                        self.all_visuals[i-1].setStyleSheet("background-color: #8E8E5A; border-radius: 12px;")

            for i in pos_ls:
                if i in self.red_leds:
                    self.all_visuals[i-1].setStyleSheet("background-color: white; border-radius: 12px;")
                else:
                    self.all_visuals[i-1].setStyleSheet("background-color: white; border-radius: 12px;")
            
            
            

    def ledprint(self,pos):
            name = self.leds[pos]
            print(f"{name.text()} is checked: {name.isChecked()}")

    def send_preset(self,item):
            try:
                f = self.presets[item]
                if item <= len(self.presets):
                    print("sending item: "+f)
                    send_serial(f)
                else:
                    print(f'Someting went wrong, button {item} has no associated preset')
            except Exception as e:
                print(f'Error:{e}')

    def send_strobe(self,time):
            preset = self.selected_label.currentText()
            print(f"Sending: {preset} , {time}")
            send_serial(f"{preset} {time}")

        

    def send_animation(self,item):
            try:
                f = self.animations[item]
                if item <= len(self.presets):
                    print("sending animation: "+f)
                    send_serial(f)
                else:
                    print(f'Someting went wrong, button {item} has no associated preset')
            except Exception as e:
                print(f'Error:{e}')

    def set_visual_null(self):
            send_serial("empty")
            print("setting visual")
            for i in range(1,26):
                if i in self.red_leds:
                    self.all_visuals[i-1].setStyleSheet("background-color: #8E5A5A; border-radius: 12px;")
                else:
                    self.all_visuals[i-1].setStyleSheet("background-color: #8E8E5A; border-radius: 12px;")



        
     
    



     
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LightControl()
    apply_dark_theme(app)
    window.show()
    sys.exit(app.exec_())