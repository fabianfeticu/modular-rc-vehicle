from cProfile import label
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
import sys
import time 

#this is a file designed for testing different GUI elements

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.setWindowTitle(" ")
        self.setFixedSize(QSize(1250, 750))
        self.window_titles = [
            'My App',
            'My App1',
            'Still My App',
            'Still My App1',
            'What on earth',
            'What on earth1',
            'This is surprising',
            'This is surprising1',
            'Something went wrong'
        ]


        self.button = QPushButton("Change Title")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: lightgreen;
            }
            QPushButton:pressed {
                background-color: red;
               
            }
        """)

        self.button.setCheckable(True)
        self.button1 = QPushButton("Change")
        self.button1.setCheckable(True)
    

        self.label = QLabel
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        self.input.setFixedSize(100,30)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
       
        central_widget.setStyleSheet('''
        
        background-color: lightblue;
                                           
        ''')
        
        main_layout = QVBoxLayout()
        second_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        main_layout.addWidget(self.button)
        main_layout.addStretch()
        second_layout.addStretch()
        second_layout.addWidget(self.input)
        #
        second_layout.addStretch()
        main_layout.addLayout(second_layout)
        main_layout.addStretch()
        
        
        self.button.clicked.connect(self.click)
    


 

"""
     def click(self):
            try:
                if self.label.text() != 0:
                    self.setWindowTitle(self.label.text())
                else:
                    self.setWindowTitle(self.window_titles[self.i])
                    self.i+=1
            except:
                 print("no")
                """
        
        
"""

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

    


"""




app = QApplication(sys.argv)
app.setStyle("Fuison")
window = MainWindow()
window.show()  


app.exec()

