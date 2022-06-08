import json

data = {
    'monthes': {
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
    },
    'even_week': {
        'понедельник': ('Боги Олимпа', 'Легенда моря'),
        'вторник': ('Охотники за привидениями', 'Веселее вместе'),
        'среда': ('Большая стройка', 'Однажды в Довиле'),
        'четверг': ('Мудрый пират', 'Остров сокровищ'),
        'пятница': ('Сын царя Музарби', 'Песни  о главном'),
        'суббота': ('Величайшее шоу  Мадагаскара', 'Созведие талантов'),
        'воскресенье': ('Неуловимый Фунтик', 'День волшебства'),
    },
    'odd_week': {
        'понедельник': ('Маркиз Карабас и Кот в сапогах', 'Вечеринка fête blanche'),
        'вторник': ('Шоу мыльных пузырей', 'Быстрее Выше Сильнее'),
        'среда': ('Бременские музыканты', 'Стиляги'),
        'четверг': ('Атлантида', 'Аквалатино'),
        'пятница': ('Казак Митрошка и Лихо - немножко', 'Цветущий край'),
        'суббота': ('Короли вечеринок', 'Академ шоу'),
        'воскресенье': ('Время для счастья', 'Топ-10 танцевальный марафон'),
    },
    'ads': [],
}


def create_json_data():
    with open('jdata.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


create_json_data()