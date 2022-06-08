import json
import locale

from datetime import datetime

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

with open('jdata.json') as file:
    open_data = json.load(file)


def get_weekday_date():
    today = datetime.today()
    str_today = datetime.today().strftime('%A, %d').lower()
    str_day_month = str(today.month)
    return f'Добро пожаловать в отель Довиль! Сегодня {str_today} {open_data["monthes"][str_day_month]}'


def get_show():
    today = datetime.today()
    weekday = today.strftime('%A').lower()
    number_week = today.isocalendar()[1]
    if number_week % 2 == 0:
        info = f'РАСПИСАНИЕ: Минидиско - 19:30 | ' \
               f'Награждение - 19:45 | ' \
               f'Детская вечерняя программа: {open_data["even_week"][weekday][0]} - 20:00 | ' \
               f'Взрослая вечерняя программа: {open_data["even_week"][weekday][1]} - 21:00 | '
        return info
    else:
        info = f'РАСПИСАНИЕ: Минидиско - 19:30 | ' \
               f'Награждение - 19:45 | ' \
               f'Детская вечерняя программа: {open_data["odd_week"][weekday][0]} - 20:00 | ' \
               f'Взрослая вечерняя программа: {open_data["odd_week"][weekday][1]} - 21:00 | '
        return info


list_message = [get_weekday_date(), get_show()]
list_ads = [
    # 'В связи с вероятностью выпадения осадков, вечерние мероприятия переносятся на террасу снек-бара Марини',
    'Погода: воздух + 24, вода + 21, переменная облачность.',
]

message = ' | '.join(list_message)
ads = ' | '.join(list_ads)

# не работает из-за санкций
# def get_weather():
#     owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')
#     manager = owm.weather_manager()
#     observation = manager.weather_at_place("Анапа, Россия")
#     weather = observation.weather
#     temp = weather.temperature('celsius')['temp']
#     detailed = weather.clouds
#     weather_message = f'Погода: +{str(round(temp))} C, облачность: {detailed}%'
#     return weather_message
