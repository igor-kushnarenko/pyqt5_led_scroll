import json
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtCore import QTimer, Qt, QRect, QSize
from PyQt5 import QtWidgets

from pars import ads, message


class myApp(QWidget):
    def __init__(self, message, speed, start_point):
        QMainWindow.__init__(self)
        self.message = message
        self.SPEED = speed
        self.length_message = len(self.message) * 15
        self.start_point = start_point
        self.init_ui()

    def init_ui(self):
        self.timer = QTimer(self)
        self.X = 2000
        self.Y = 50
        self.FONT_SIZE = 25

        self.setWindowTitle('Doville news')
        self.setGeometry(0, self.start_point, self.X, self.Y)
        # self.setStyleSheet("background-color: black")
        self.setWindowFlags(Qt.FramelessWindowHint)  # убрали шапку окна

        wallpaper = QImage("files/wall5.jpg")
        sImage = wallpaper.scaled(QSize(self.X, self.Y))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.label = QLabel(self.message, self)
        self.label.setStyleSheet('color: white')
        self.label_x = self.X - 50
        self.lable_y = 8
        self.label.move(self.label_x, self.lable_y)
        self.label.setFont(QFont('Ubuntu', self.FONT_SIZE))

        if self.timer.isActive():
            self.timer.stop()
            self.timer.timeout.disconnect()
            self.timer.start(self.SPEED)
            self.timer.timeout.connect(self.move_label_left)
        else:
            self.timer.start(self.SPEED)
            self.timer.timeout.connect(self.move_label_left)

    def move_label_left(self):
        if self.label_x == -(self.length_message + self.X):
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
        self.create_send_btn()
        self.create_text_field()
        self.send_command()

    def init_ui(self):
        self.X = 400
        self.Y = 400
        self.setGeometry(300, 300, self.X, self.Y)
        self.setWindowTitle('Led roll')
        text = 'Добавьте объявление'
        self.label = QLabel(text, self)
        self.label.move(10, 5)
        self.label.adjustSize()
        self.list_messages_lbl()

    def list_messages_lbl(self):
        """
        Отображение на окне списка сообщений отправленных пользователем в базу.
        """
        y = 100
        with open('jdata.json') as file:
            res = json.load(file)
            for message in res['ads']:
                self.m_lbl = QLabel(message, self)
                self.m_lbl.move(10, y)
                y += 20
                self.m_lbl.adjustSize()

    def create_send_btn(self):
        self.btn = QtWidgets.QPushButton('Отправить', self)
        self.btn.move(self.X // 2 - 50, 60)
        self.btn.setFixedSize(120, 22)

    def create_text_field(self):
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QRect(50, 30, 300, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

    def send_command(self):
        self.btn.clicked.connect(lambda: self.send_message_to_line(self.lineEdit.text().upper()))

    def send_message_to_line(self, message):
        ads_window.length_message = 15 * len(message)
        ads_window.label.setText(message)
        ads_window.label.adjustSize()
        # self.add_message_to_file(message)

    def add_message_to_file(self, message):
        """
        Добавление сообщений отправленных пользователем в базу.
        :param message:
        :return:
        """
        with open('jdata.json') as file:
            res = json.load(file)
            res['ads'].append(message)
            print(res['ads'])
        with open('jdata.json', 'w') as jfile:
            json.dump(res, jfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex_window = myApp(message, speed=15, start_point=0)
    ex_window.show()
    ads_window = myApp(ads.upper(), speed=9, start_point=75)
    # ads_window = myApp(ads.upper(), speed=9, start_point=0)
    ads_window.show()
    ui_window = UserInterface()
    ui_window.show()
    sys.exit(app.exec_())
