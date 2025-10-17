from model.model import Person


"""
直接使用Model类型的get方法
"""
try:
    grandma = Person.get(Person.name == "Grandma")
    print(grandma)
except Exception as e:
    print(e)
