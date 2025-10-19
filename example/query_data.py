from peewee import fn, JOIN

from model.model import Person, Pet

# """
# 直接使用Model类型的get方法
# """
# # try:
# #     grandma = Person.get(Person.name == "Grandma")
# #     print(grandma)
# # except Exception as e:
# #     print(e)


# """
# 使用Person().select().where().get()
# """
#
# try:
#     grandma = Person.select().where(Person.name == 'Grandma L1').get()
# except Exception as e:
#     print(e)


# """
# 使用select()直接查询多行数据
# """
# try:
#     people = Person.select()
#     # for person in people:
#     #     print(person.name)
#     print(people)       # TODO 这里select返回的是什么类型的数据,为什么直接print啥也没有呢?
# except Exception as e:
#     print(e)
#
# try:
#     pets = Pet.select().where(Pet.animal_type == "cat")
#     for pet in pets:
#         print(pet.name,pet.owner.name)
# except Exception as e:
#     print(e)


# """
# 主表查询出来以后,直接可以统计从表(这的表述存在错误性,并不是直接统计,而是在调用person.pets.count()的时候会再次向mysqld发送sql进行查询
# """
# try:
#     people = Person.select()
#     for person in people:
#         print(f"{person.name:<10},{person.pets.count():>2}")    #这里使用person.pets的时候会根据person.id的再去数据库查询一次,如果用prefetch就不会
# except Exception as e:
#     print(e)
#
# # 比较非prefetch和prefetch的方式,区别在于prefetch以后,pets字段上已经填充好了数据,同时仅向数据库发送两条sql而已.
# # 非prefetch的方式每一个person都需要单独查一次pet表.
# try:
#     people = Person.select().prefetch(Pet)
#     for person in people:
#         print(f"{person.name:<10},{len(person.pets):>2}")    #这里使用person.pets的时候会根据person.id的再去数据库查询一次,如果用prefetch就不会
# except Exception as e:
#     print(e)


# """
# join查询,但是仅仅用join方法指明两个表进行连接,但是并没有指定在哪些字段上进行连接,自动用了外键和外键参照字段连接
# """
#
# query =  Person.select(Person,Pet).join(Pet,JOIN.LEFT_OUTER).order_by(Person.name,Pet.name)
# for person in query:
#     if hasattr(person,"pet"):
#         print(person.name, person.pet.name)
#     else:
#         print(person.name,"not pet")


# """
# has_many关系中使用prefetch,将多个从表记录关联到一个主表记录上
# """
# people = Person.select().where(Person.name == "Bob").prefetch(Pet)
# for person in people:
#     print(person.name)
#     for pet in person.pets:
#         print("*",pet.name)