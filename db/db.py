import logging

from peewee import *


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)

db = MySQLDatabase(
    "peewee_case",
    **{
        "host": "9.134.245.207",
        "port": 33060,
        "user": "root",
        "password": "Nwpuyaoxin94.",
        "charset": "utf8mb4",
    }
)
