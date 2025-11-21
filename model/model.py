from peewee import *
from db.db import db
from datetime import datetime
from model.dynamic_tablename import make_table_name


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    id = AutoField()
    name = CharField()
    birthday = DateField()


class Pet(BaseModel):
    owner = ForeignKeyField(model=Person, field=Person.id, backref="pets")
    name = CharField()
    animal_type = CharField()


class User(BaseModel):
    username = TextField()


class Tweet(BaseModel):
    content = TextField()
    timestamp = DateTimeField(default=datetime.now)
    user = ForeignKeyField(User, lazy_load=True)


class Event(BaseModel):
    event_date = DateField()

    class Meta:
        table_function = make_table_name
