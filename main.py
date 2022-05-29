import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtWidgets

from parser import message, ads


class myApp(QWidget):
    def __init__(self, message, speed, start_point):
        QMainWindow.__init__(self)
        self.message = message
        self.SPEED = speed
        self.start_point = start_point
        self.init_ui()

    def init_ui(self):
        self.timer = QTimer(self)
        self.X = 2000
        self.Y = 50
        self.FONT_SIZE = 25

        self.setWindowTitle('Doville news')
        self.setGeometry(0, self.start_point, self.X, self.Y)
        self.setStyleSheet("background-color: black")
        self.setWindowFlags(Qt.FramelessWindowHint) # убрали шапку окна

        self.label = QLabel(self.message, self)
        self.label.setStyleSheet('color: white')
        self.label_x = self.X - 50
        self.lable_y = 8
        self.label.move(self.label_x, self.lable_y)
        self.label.setFont(QFont('Arial', self.FONT_SIZE))

        if self.timer.isActive():
            self.timer.stop()
            self.timer.timeout.disconnect()
            self.timer.start(self.SPEED)
            self.timer.timeout.connect(self.move_label_left)
        else:
            self.timer.start(self.SPEED)
            self.timer.timeout.connect(self.move_label_left)

    def move_label_left(self):
        if self.label_x == -(15 * len(self.message) + self.X):
            self.label_x = self.X - 50
            self.label_x = self.label_x - 1
            self.label.move(self.label_x, self.lable_y)
        else:
            self.label_x = self.label_x - 1
            self.label.move(self.label_x, self.lable_y)


class UserInterface(QMainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.init_ui()
        self.send_btn()

    def init_ui(self):
        self.X = 400
        self.Y = 100
        self.setGeometry(300, 300, self.X, self.Y)
        self.setWindowTitle('Led roll')
        self.label = QLabel('Led Roll', self)
        self.label.move(self.X // 2, 20)

    def send_btn(self):
        self.btn = QtWidgets.QPushButton('Отправить', self)
        self.btn.move(self.X // 2 - 50, 70)
        self.btn.setFixedSize(120, 22)
        self.btn.clicked.connect(self.send_message)

    def send_message(self):
        print('Send message to console.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp(message, speed=15, start_point=0)
    ex.show()
    ads = myApp(ads, speed=10, start_point=75)
    ads.show()
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec_())
