#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtCore import Qt, QTimer

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
        self.X = 800
        self.Y = 50
        self.FONT_SIZE = 25

        self.setWindowTitle('Doville news')
        self.setGeometry(100, 100, 750, 100)

        self.label = QLabel(message, self)
        self.label.move(self.X, self.Y)
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
        if self.X == -(17 * len(message) + 800):
            self.X = 800
            self.X = self.X - 1
            self.label.move(self.X, self.Y)
        else:
            self.X = self.X - 1
            self.label.move(self.X, self.Y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec_())