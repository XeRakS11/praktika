import sys, random, string
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout,QLineEdit, QPushButton, QWidget
from PyQt6.QtCore import QTimer, Qt
from test import TestWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450,350)
        self.setWindowTitle("Регистрация")

        self.first_lb1=QLabel("Введите пароль")
        self.first_lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit=QLineEdit()
        self.first_lb2=QLabel("Введите логин")
        self.first_lb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit2=QLineEdit()
        self.btn=QPushButton("зарегистрироваться")
        self.btn2=QPushButton("Выйти")
        self.btn.clicked.connect(self.btn_clicked)
        self.btn2.clicked.connect(self.exit)
        self.layout=QVBoxLayout()
        widget=QWidget()

        self.layout.addWidget(self.first_lb1)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb2)
        self.layout.addWidget(self.first_lineEdit2)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.setCentralWidget(widget)
        widget.setLayout(self.layout)


        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())


    def btn_clicked(self):
        if self.first_lineEdit.text() == "1" and self.first_lineEdit2.text() == "1":
            self.sm=SM()
            self.sm.show()
        else:
            self.kapcha = Kapcha()
            self.kapcha.show()
            
    def exit(self):
        self.close()



class  WelcomeWindow(QMainWindow): 
    def __init__(self, n):
        super().__init__()
        self.lbl = QLabel(f"привет {n}")
        self.name = n
        btn = QPushButton("Пойти тест.")
        btn.clicked.connect(self.click_b)
        vbox = QVBoxLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)
        vbox.addWidget(self.lbl)
        vbox.addWidget(btn)
        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
            
    def click_b(self):
        self.test = TestWindow(self.name)
        self.test.show()
        self.close()


class Kapcha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle("Капча")
        self.setFixedSize(400, 200)
        self.len=4
        self.capcha=string.digits+string.ascii_uppercase
        rnd_string=''.join(random.sample(self.capcha, self.len))
        rnd=random.randint(1000,9999)
        self.first_lb1=QLabel("Captcha")
        self.first_lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit=QLineEdit()
        self.first_lb12=QLabel(str(rnd_string))
        self.btn=QPushButton("Проверка")
        self.btn.clicked.connect(self.btn_clicked)

        self.timer_label=QLabel("Таймер:")
        self.timer=QTimer()
        self.timer_counter = 4
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_tick)
 
        self.layout=QVBoxLayout()
        widget=QWidget()

        self.layout.addWidget(self.first_lb1)
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb12)
        self.layout.addWidget(self.btn)
        self.setCentralWidget(widget)
        widget.setLayout(self.layout)

        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
    def btn_clicked(self):
        if self.first_lineEdit.text() == self.first_lb12.text():
            self.close()
        else:
            self.timer.start()
            self.btn.setEnabled(False)   
            
    def timer_start(self):
        self.timer_counter = 5
        self.timer.start()
        
    def timer_tick(self):
        self.timer.start(1000)
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")
        self.first_lb12.setText("")

        if self.timer_counter == 0 :

            self.timer.stop()
            self.timer_counter=4
            self.btn.setEnabled(True)
            rnd_string=''.join(random.sample(self.capcha, self.len))
            self.first_lb12.setText(str(rnd_string))
            
class SM(QMainWindow):#3-е окно
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,230)
        self.setWindowTitle("вход")

        self.first_lb1=QLabel("Введите имя и фамилию")
        self.first_lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit=QLineEdit()
        self.first_lb2=QLabel("Введите группу")
        self.first_lb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit2=QLineEdit()
        self.name = self.first_lineEdit
        group = self.first_lineEdit2
        self.btn=QPushButton("Войти")
        self.btn2=QPushButton("Выйти")
        self.btn.clicked.connect(self.btn_clicked)
        self.btn2.clicked.connect(self.exit)
        self.layout=QVBoxLayout()
        widget=QWidget()

        self.layout.addWidget(self.first_lb1)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb2)
        self.layout.addWidget(self.first_lineEdit2)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.setCentralWidget(widget)
        widget.setLayout(self.layout)


        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())


    def btn_clicked(self):
            self.test=WelcomeWindow(self.name.text())
            self.test.show()

    def exit(self):
        self.close()
            
app=QApplication(sys.argv)
window=Main()
window.show()
app.exec()