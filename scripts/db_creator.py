import peewee

from scripts import db_models

if __name__ == '__main__':
    try:
        db_models.db.connect()
        db_models.LedLine.create_table()
    except peewee.InternalError as ex:
        print(str(ex))


def add_message_to_db(is_active, message):
    return db_models.LedLine.create(
        is_active=is_active,
        message=message
    )


add_message_to_db(False, 'Открытие сезона 2023!')
