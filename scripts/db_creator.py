import peewee

from scripts import db_models

if __name__ == '__main__':
    try:
        db_models.db.connect()
        db_models.LedLine.create_table()
    except peewee.InternalError as ex:
        print(str(ex))
