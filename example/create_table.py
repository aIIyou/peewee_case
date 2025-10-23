from db.db import db
from model.model import Person, Pet, Event

db.create_tables(models=[Event])
