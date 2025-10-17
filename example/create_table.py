from db.db import db
from model.model import Person, Pet


db.create_tables(models=[Person, Pet])
