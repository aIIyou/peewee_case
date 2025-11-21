import logging
import random

import string
from datetime import datetime

from peewee import *


import stringcase

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)


def make_table_name(model_class) -> str:
    characters = string.ascii_letters + string.digits
    suffix = "".join(random.choice(characters) for _ in range(8))
    return (
        stringcase.snakecase(model_class.__name__)
        + "_"
        + datetime.now().strftime("%Y_%m_%d")
        + "_"
        + suffix
    )


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


class BaseModel(Model):
    class Meta:
        database = db


class PlayerProfiles(BaseModel):
    id = IntegerField(primary_key=True)

    meeting = IntegerField()

    listing = DecimalField()

    voucher = IntegerField()

    account = IntegerField()

    cart = CharField()

    delivery = IntegerField()

    player = IntegerField()

    class Meta:
        table_function = make_table_name


def add_new_player_profile(meeting, listing, voucher, account, cart, delivery, player):

    return create_player_profile(
        meeting, listing, voucher, account, cart, delivery, player
    )


def create_player_profile(meeting, listing, voucher, account, cart, delivery, player):

    profile = PlayerProfiles(
        meeting=meeting,
        listing=listing,
        voucher=voucher,
        account=account,
        cart=cart,
        delivery=delivery,
        player=player,
    )
    profile.save()
    return profile


def filter_sql_list(sql_list):
    """
    过滤sql_list，只保留真正的SQL语句
    """
    if not sql_list or not isinstance(sql_list, list):
        return []

    def preprocess_sql(sql):
        """
        预处理SQL字符串，处理DEBUG:peewee格式的日志
        """
        if not isinstance(sql, str):
            return sql

        # 匹配 DEBUG:peewee:('SQL语句', [参数列表]) 格式
        import re

        pattern = r"^DEBUG:peewee:\('([^']+)',\s*\[[^\]]*\]\)$"
        match = re.match(pattern, sql.strip())

        if match:
            # 提取SQL语句部分
            sql_statement = match.group(1)
            # 将 %s 替换为 ?
            sql_statement = sql_statement.replace("%s", "?")
            return sql_statement
        else:
            # 如果不是DEBUG格式，直接返回原SQL
            return sql

    # 先预处理所有SQL语句
    processed_sql_list = [preprocess_sql(sql) for sql in sql_list]

    # 然后使用SqlParser进行过滤
    return processed_sql_list


def main():
    try:
        add_new_player_profile("", "", "", "", "", "", "")
    except Exception:
        print("")


if __name__ == "__main__":
    print(
        filter_sql_list(
            [
                """DEBUG:peewee:('INSERT INTO `player_profiles_2025_11_20-Dw1fL8ik` (`meeting`, `listing`, `voucher`, `account`, `cart`, `delivery`, `player`) VALUES (%s, %s, %s, %s, %s, %s, %s)', ['', Decimal('0'), '', '', '', '', ''])
"""
            ]
        )
    )
