import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

list_message = ['Добро пожаловать в Отель Довиль!', 'Сегодня вторник, 24 мая.',
           'В СВЯЗИ С ПОГОДНЫМИ УСЛОВИЯМИ ПРОВЕДЕНИЕ ВЕЧЕРНИХ МЕРОПРИЯТИЙ ПЕРЕНОСИТСЯ НА ТЕРРАСУ МАРИНИ.']
message = ' '.join(list_message)


class myApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.SPEED = 5
        self.timer = QTimer(self)
        self.X = 1000
        self.Y = 50
        self.FONT_SIZE = 25

        self.setWindowTitle('Doville news')
        self.setGeometry(100, 100, self.X, self.Y)

        self.label = QLabel(message, self)
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
        if self.label_x == -(17 * len(message) + self.X):
            self.label_x = 800
            self.label_x = self.label_x - 1
            self.label.move(self.label_x, self.lable_y)
        else:
            self.label_x = self.label_x - 1
            self.label.move(self.label_x, self.lable_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec_())