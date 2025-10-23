"""
这个例子主要测试一下直接从一个datetime字段查出来day
"""

from datetime import datetime

from model.model import Event

now = datetime.now()

Event.select(Event.event_date.day.alias("day")).where(
    (Event.event_date.year == now.year) & (Event.event_date.month == now.month)
).execute()

"""
peewee会使用EXTRACT 函数从date字段取出year,month,day
SELECT EXTRACT(day FROM `t1`.`event_date`) AS `day` FROM `event` AS `t1` 
WHERE (
(EXTRACT(year FROM `t1`.`event_date`) = 2025) 
AND 
(EXTRACT(month FROM `t1`.`event_date`) = 10)
)
"""
