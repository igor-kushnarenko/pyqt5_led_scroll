import peewee


user = 'postgres'
password = 5280
db_name = 'ledline_db'
host = 'localhost'

db = peewee.PostgresqlDatabase(
    database=db_name,
    user=user,
    password=password,
    host=host
)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class LedLine(BaseModel):
    id = peewee.PrimaryKeyField(null=True)
    is_active = peewee.BooleanField(null=True)
    message = peewee.TextField()

    class Meta:
        db_table = 'led_line'
