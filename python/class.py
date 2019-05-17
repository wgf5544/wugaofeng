class a(object):
    pass

print("a type:", a.__class__)
print("a bases:", a.__bases__)  # 旧式类的类型为老式：classobj，在python3.x中所有类的类型为新式类：type

print("list type:", list.__class__)  # <class 'type'> 被type类实例化的

print("list bases:", list.__bases__)  # 父类是什么,父类可能是多个，所以返回类型是tuple

print("type bases:", type.__bases__)
mylist = [1, 3, 4]
print(mylist.__class__)
# print(mylist.__bases__)
# metaclass->class->instance