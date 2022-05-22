#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtCore import Qt, QTimer

message = "Добро пожаловать в отель Довиль! Рады видеть вас на наших мероприятиях. Сегодня вечером!" \
          "Добро пожаловать в отель Довиль! Рады видеть вас на наших мероприятиях. Сегодня вечером! NHEEEE"


class myApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.speed = 25
        self.timer = QTimer(self)
        btn_start = QPushButton("start", self)
        btn_start.move(10, 10)
        self.x = 800
        self.y = 50
        self.setWindowTitle("Наши новости")
        self.label = QLabel(message, self)
        self.label.move(self.x, self.y)
        self.label.setFont(QFont('Arial', 20))
        self.setGeometry(100, 100, 750, 100)

        btn_start.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == "start":
            if self.timer.isActive():
                self.timer.stop()
                self.timer.timeout.disconnect()
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_left)
            else:
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_left)

    def move_label_left(self):
        if self.x == -(5 * len(message) + 800):
            self.x = 800
            self.x = self.x - 1
            self.label.move(self.x, self.y)
        else:
            self.x = self.x - 1
            self.label.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec_())