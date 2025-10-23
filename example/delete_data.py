from model.model import Pet, Person

"""
在pet模型中定义外键时指定了on_delete="CASCADE"，所以，此时删除person，会把关联到的pet也删除
"""
uncle_bob = Person.get(Person.name == "Bob")
uncle_bob.delete_instance(recursive=True)
