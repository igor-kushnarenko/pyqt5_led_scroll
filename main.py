import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt

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
        self.X = 1500
        self.Y = 50
        self.FONT_SIZE = 25

        self.setWindowTitle('Doville news')
        self.setGeometry(0, self.start_point, self.X, self.Y)
        self.setStyleSheet("background-color: black")
        self.setWindowFlags(Qt.FramelessWindowHint) # убрать шапку

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

        self.show()

    def move_label_left(self):
        if self.label_x == -(15 * len(self.message) + self.X):
            self.label_x = self.X - 50
            self.label_x = self.label_x - 1
            self.label.move(self.label_x, self.lable_y)
        else:
            self.label_x = self.label_x - 1
            self.label.move(self.label_x, self.lable_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp(message, speed=10, start_point=0)
    ads = myApp(ads, speed=15, start_point=75)
    sys.exit(app.exec_())
