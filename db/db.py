import logging

from peewee import *


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)

db = MySQLDatabase(
    "peewee_case",
    **{
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "Nwpuyaoxin94.",
        "charset": "utf8mb4",
    }
)
