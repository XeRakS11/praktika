from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QApplication, QMainWindow
from test import TestWindow

class  WelcomeWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        lbl = QLabel("Добро пожаловать на минитест!")
        btn = QPushButton("Погнали")
        btn.clicked.connect(self.click_b)
        vbox = QVBoxLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)
        vbox.addWidget(lbl)
        vbox.addWidget(btn)
        with open("styles\style.css", "r") as css:
            self.setStyleSheet(css.read())
            
    def click_b(self):
        self.test = TestWindow()
        self.test.show()
        self.close()