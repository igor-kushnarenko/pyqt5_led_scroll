import json
import locale
import os

from datetime import datetime

import pyowm

from initial_data import create_json_data

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

file_path = "jdata.json"

if os.path.exists(file_path):
    with open('jdata.json') as file:
        open_data = json.load(file)
else:
    create_json_data()


def weather_parser():
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
    today = datetime.today()
    str_today = datetime.today().strftime('%A, %d').lower()
    str_day_month = str(today.month)
    return f'Добро пожаловать в отель Довиль! Сегодня {str_today} {open_data["monthes"][str_day_month]}'


def get_week_info(week_type, weekday):
    text = f'РАСПИСАНИЕ: Минидиско - 19:30 | Награждение - 20:00 | ' \
                f'Детская вечерняя программа: {open_data[week_type][weekday][0]} - 20:15 | ' \
                f'Взрослая вечерняя программа: {open_data[week_type][weekday][1]} - 21:00 | '
    return text


def get_show():
    today = datetime.today()
    weekday = today.strftime('%A').lower()
    number_week = today.isocalendar()[1]
    if number_week % 2 == 0:
        week_type = 'even_week'
    else:
        week_type = 'odd_week'
    return get_week_info(week_type, weekday)


list_message = [get_weekday_date(), weather_parser(), get_show()]

# добавляется в ручную, пока
list_ads = [
    'Рады видеть вас на наших анимационных мероприятиях!',
]

message = ' | '.join(list_message)
ads = ' | '.join(list_ads)
