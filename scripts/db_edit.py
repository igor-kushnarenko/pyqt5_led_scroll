from scripts.db_models import LedLine


def add_message_to_db(message):
    """Функция реализует создание записи в БД"""
    return LedLine.create(
        message=message
    )


def delete_all_message_in_db():
    """Функция удаляющая все записи в таблице"""
    for row in LedLine.select():
        row.delete_instance()


def delete_one_message_in_db(id):
    """Функция удаляющая необходимую запись в таблице"""
    row = LedLine.select().where(LedLine.id == id).get()
    row.delete_instance()


def read_db_how_string():
    row_list = []
    for row in LedLine.select():
        row_list.append(row.message)
    return row_list


def read_db_how_row():
    row_list = []
    for row in LedLine.select():
        row_list.append(row)
    return row_list
