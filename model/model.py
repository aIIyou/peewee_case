from peewee import *
from db.db import db


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
