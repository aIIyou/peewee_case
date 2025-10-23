from db.db import db
from model.model import User, Tweet

db.create_tables(models=[User, Tweet])
