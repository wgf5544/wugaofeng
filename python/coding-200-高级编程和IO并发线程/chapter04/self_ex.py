#自省是通过一定的机制查询到对象的内部结构
from chapter04.class_method import Date
class Person:
    """
    人
    """
    name = "user"

class Student(Person):
    '''
    你好
    '''
    def __init__(self, scool_name):
        self.scool_name = scool_name

    def get_ss(self):
        pass

if __name__ == "__main__":
    user = Student("慕课网")
    '''
    nihao
    '''
    #通过__dict__查询属性
    print(user.__dict__)
    print(dir(user))
    # user.__dict__["school_addr"] = "北京市"
    # print(user.school_addr)
    print(Person.__dict__)
    # print(user.name)
    a = [1,2]
    print(dir(a))

