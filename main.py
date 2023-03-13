import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtCore import QTimer, Qt, QRect, QSize
from PyQt5 import QtWidgets

from pars import message, ads, message_from_db

from scripts.db_edit import add_message_to_db


class myApp(QWidget):
    """Класс реализующий бегущую строку"""
    def __init__(self, message, speed, start_point):
        QMainWindow.__init__(self)
        self.message = message
        self.SPEED = speed
        self.length_message = len(self.message) * 15
        self.start_point = start_point
        self.init_ui()

    def init_ui(self):
        """Иницилизация основных параметров окна"""
        self.timer = QTimer(self)
        self.X = 3000
        self.Y = 90
        self.FONT_SIZE = 25

        self.setWindowTitle('Doville news')
        self.setGeometry(0, self.start_point, self.X, self.Y)
        self.setStyleSheet("background-color: black")
        self.setWindowFlags(Qt.FramelessWindowHint)  # убрали шапку окна

        self.label = QLabel(self.message, self)
        self.label.setStyleSheet('color: #085d69')
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
        """Метод описывающий смещение текста в окне"""
        if self.label_x == -(self.length_message + self.X):
            self.label_x = self.X - 50
            self.label_x = self.label_x - 5
            self.label.move(self.label_x, self.lable_y)
        else:
            self.label_x = self.label_x - 5
            self.label.move(self.label_x, self.lable_y)

    def set_wallpaper(self):
        """Метод добавляющий фоновое изображение на бегущую строку"""
        wallpaper = QImage("C:\\Users\\honor\\PycharmProjects\\pyqt5_led_scroll\\files\\wall5.jpg")
        sImage = wallpaper.scaled(QSize(self.X, self.Y))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)


class UserInterface(QMainWindow):
    """Класс создающий окно для добавления объявления"""
    def __init__(self):
        super(UserInterface, self).__init__()
        self.init_ui()
        self.create_send_btn()
        self.create_text_field()
        self.send_command()

    def init_ui(self):
        """Метод описывающий основные параметры окна"""
        self.X = 400
        self.Y = 100
        self.setGeometry(300, 300, self.X, self.Y)
        self.setWindowTitle('Led roll')
        text = 'Добавьте объявление'
        self.label = QLabel(text, self)
        self.label.move(10, 5)
        self.label.adjustSize()

    def create_send_btn(self):
        """Метод реализующий кнопку для отправки объявления"""
        self.btn = QtWidgets.QPushButton('Отправить', self)
        self.btn.move(self.X // 2 - 50, 60)
        self.btn.setFixedSize(120, 22)

    def create_text_field(self):
        """Метод реализующий поле для ввода текста объявления"""
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QRect(50, 30, 300, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

    def send_command(self):
        """Метод реализующий действие по нажатию кнопки"""
        self.btn.clicked.connect(lambda: self.send_message_to_line(self.lineEdit.text().upper()))

    def send_message_to_line(self, message):
        """Метод отправляющий объявление в бегущую строку"""
        # добавление записи в БД
        add_message_to_db(message)

        ads_window = myApp(message_from_db, speed=9, start_point=80)
        ads_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # реализация окона бегущей строки с готовыми сообщениями
    ledline_window = myApp(message, speed=15, start_point=0)
    ledline_window.show()

    # реализация окона бегущей строки с объявлениями
    ads_window = myApp(message_from_db, speed=1, start_point=80)
    ads_window.show()

    # реализация окна для ввода объявления
    ui_window = UserInterface()
    ui_window.show()
    sys.exit(app.exec_())
