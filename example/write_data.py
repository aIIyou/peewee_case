from datetime import date

from model.model import Person
from util.fomat_print import Printer


# """
# 这里因为指定了主键id=2,所以save方法就映射到update 语句
# """
# p = Person(id=2, name="na", birthday=date(2020, 10, 24))
# print(p.save())


# """
# 这里没有指定主键，所以save方法就映射到insert into语句
# """
# p = Person(name="rookie", birthday=date(1998, 1, 1))
# p.save()


# """
# 直接用类的方法create插入数据
# """
# grandma = Person.create(name="Grandma", birthday=date(1935, 3, 1))
# herb = Person.create(name="Herb", birthday=date(1950, 5, 5))
