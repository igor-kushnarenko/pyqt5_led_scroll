import pyowm

import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

monthes = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря',
}

even_week = {
    'понедельник': ('Миньоны', 'Веселее вместе'),
    'вторник': ('Легенда семи морей', 'Водный мир'),
    'среда': ('Гарри Поттер', 'Чародеи'),
    'четверг': ('Монстры на каникулах', 'Балканы'),
    'пятница': ('Минидиско', 'Созвездие талантов'),
    'суббота': ('Фердинанд', 'Испания'),
    'воскресенье': ('Магическое перо', 'День волшебства'),

}
odd_week = {
    'понедельник': ('Приключения Фараона', 'Сокровища Нила'),
    'вторник': ('Каникулы Ули и Кнопки', 'Цирк'),
    'среда': ('Головоломка', 'Курорт представляет'),
    'четверг': ('Иван да Марья', 'Кубань'),
    'пятница': ('Минидиско', 'Созвездие талантов'),
    'суббота': ('Барбоскины', 'Спорт-драйв'),
    'воскресенье': ('Фунтик', 'В гостях у сказки'),

}


def get_weekday_date():
    today = datetime.today()
    str_today = datetime.today().strftime('%A, %d').lower()
    return f'Добро пожаловать в отель Довиль! Сегодня {str_today} {monthes[today.month]}'


def get_show():
    today = datetime.today()
    weekday = today.strftime('%A').lower()
    number_week = today.isocalendar()[1]
    if number_week % 2 == 0:
        info = f'РАСПИСАНИЕ: Детская вечерняя программа: {even_week[weekday][0]} - 20:00, ' \
               f'Взрослая вечерняя программа: {even_week[weekday][1]} - 21:00. '
        return info
    else:
        info = f'РАСПИСАНИЕ: Детская вечерняя программа: {odd_week[weekday][0]} - 20:00, ' \
               f'Взрослая вечерняя программа: {odd_week[weekday][1]} - 21:00. '
        return info

list_message = [get_weekday_date(), get_show()]
list_message.append('В сзяви с погодными условиями все переносится на террасу Марини! Следите за новостями.')

message = ' | '.join(list_message)

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
