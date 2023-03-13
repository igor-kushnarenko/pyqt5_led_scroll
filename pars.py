import json
import locale
import os
from datetime import datetime

import pyowm

from initial_data import create_json_data
from scripts.db_edit import read_db_how_row


locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
file_path = "jdata.json"
today = datetime.today()

if os.path.exists(file_path):
    with open('jdata.json', 'r') as file:
        open_data = json.load(file)
else:
    create_json_data()


def weather_parser():
    """Функция которая запрашивает и формирует прогноз погоды"""
    global weather

    def get_weather():
        owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')
        manager = owm.weather_manager()
        observation = manager.weather_at_place("Анапа, Россия")
        weather = observation.weather
        temp = weather.temperature('celsius')['temp']
        detailed = weather.clouds
        weather_message = f'Погода: +{str(round(temp))} C, облачность: {detailed}%'
        return weather_message

    try:
        weather = get_weather()
    except:
        weather = 'Погода: воздух + 24, вода + 21, переменная облачность.'

    return weather


def get_weekday_date():
    """Функция возвращающая приветственное сообщение"""
    str_today = datetime.today().strftime('%A, %d').lower()
    str_day_month = str(today.month)
    return f'Добро пожаловать в отель Довиль! Сегодня {str_today} {open_data["monthes"][str_day_month]}'


def get_show():
    """Функция возвращающая расписание"""
    weekday = today.strftime('%A').lower()
    number_week = today.isocalendar()[1]
    if number_week % 2 == 0:
        week_type = 'even_week'
    else:
        week_type = 'odd_week'

    text = f'РАСПИСАНИЕ: Награждение - 19:30 | ' \
           f'Детская вечерняя программа: {open_data[week_type][weekday][0]} - 19:45 | ' \
           f'Взрослая вечерняя программа: {open_data[week_type][weekday][1]} - 20:30 | '
    return text


list_message = [get_weekday_date(), weather_parser(), get_show()]

# добавляется в ручную, пока
# todo Объявления будем добавлять в postgresql и работать уже с ней
list_ads = [
    'Рады видеть вас на наших анимационных мероприятиях!',
]

message = ' | '.join(list_message)
ads = ' | '.join(list_ads)

m = []
for r in read_db_how_row():
    m.append(r.message)
message_from_db = ' | '.join(m)