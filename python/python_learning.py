# ==============class================

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
# 所有类的父类（包括type）都是object
# type实例化了自己，同时实例化了object






# ====================变量和动态特性=====================

# python中类型变量主要包括Number（数字）、String（字符串）、List（列表）、Tuple（元组）和Dictionary（字典）等


print(type(3j+1))

# 动态特性：变量预先不需要声明类型就可以使用
"""
静态编译：以C语言为例，变量根据类型预先分配的地址是内存空间中的一个固定位置，改变值的时候，地址并不会变

动态编译：变量赋值时，首先解释器会给这个值分配内存空间，然后将变量指向这个值的地址；
        改变值时，解释器会给新值分配另一个内存空间，再将变量指向这个新值的地址。
        所以python中改变的是变量所指向的地址，而内存空间中的值是固定不变的。
id():查看变量的内存地址
相同值不可变类型的变量，地址相同；相同值包含可变类型值的变量，地址不同
相同值可变类型的变量，地址不同；

可变类型：列表，字典；相同值分配不同的地址，改变值时，地址不会变。
不可变类型：整数、浮点数、字符串、元组；相同值分配相同地址，改变值时，地址发生改变，并将原来的变量指向新的地址；

如果没有其他变量引用原有对象，原有对象就会被回收。
以上就是python作为动态类型语言的特点。


"""
i = 10000000000000000000000000000000000000000000000000000000000000
j = 10000000000000000000000000000000000000000000000000000000000000
print(hex(id(i)))  # 以16进制显示地址
print(hex(id(j)))

s1 = 'a'*1
s2 = 'a'*1
print(hex(id(s1)), hex(id(s2)))

t1 = (2, 3, '3', (0,), [])
t2 = (2, 3, '3', (0,), [])

print(hex(id(t1)), hex(id(t2)))

l1 = []
l2 = []
print(hex(id(l1)), hex(id(l2)))


# ===============继承、派生、和组合=================
"""
继承、派生：在不改变“类”代码的基础上改变原有的功能，实现代码的重用。
    父类和子类的关系是一种“是”的关系，
    比如程序员是人类，也就是程序员继承人类的属性，对象有很多共同属性时，可以抽象成一个超类，用来继承。

组合方式：可以将其他类作为属性加入到类中来扩展自己的属性资源，有效利用其他类的资源，增强代码的可重用性。
    组合建立的类和组合类之间的关系是一种“有”的关系，比如程序员有电脑、会编程，而人类并不一定都具备。
"""


class ParentClass1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('speak ParentClass1')


class SubClass1(ParentClass1):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    # 新增write()方法
    def write(self):
        print('write SubClass1')


cls = SubClass1("wgf", 23, "中国")
cls.speak()
cls.write()
print(cls.age)

# ============进程和线程============

"""
进程和线程：程序是存储在磁盘上的可执行文件，当被加载到内存中并被操作系统调用时，它就有了生命周期，进程就是运行中的程序。
一个进程可以并行运行多个线程，每个线程执行不同的任务，线程是进程组成部分；
一个进程启动时至少要执行一个任务，因此至少有一个主线程，由主线程再创建其他的子线程。

每个进程都拥有自己的地址空间、内存和数据栈，由操作系统管理所有的进程，并为其合理分配执行时间。
进程间资源相互独立，不同进程间需要通过IPC（进程间通信）方式共享信息，单个进程崩溃不会导致系统崩溃。

多线程在同一个进程下执行的，共享同一片数据空间，相比于进程而言，线程间信息共享更加容易，当一个线程崩溃时会导致进程崩溃。

多线程的执行方式主要由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来像是同时执行一样。
多核CPU真正意义上实现多线程或多进程的同时执行。
"""

from threading import Thread
from multiprocessing import Process,Manager
from timeit import timeit


# 计算密集型任务
def count(n):
    while n > 0:
        n -= 1


# 不采用多任务方式
def test_normal():
    count(1000000)
    count(1000000)


# 多线程方式
def test_Thread():
    t1 = Thread(target=count,args=(1000000,))
    t2 = Thread(target=count,args=(1000000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 多进程方式
def test_Process():
    t1 = Process(target=count,args=(1000000,))
    t2 = Process(target=count,args=(1000000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    # print("test_normal", timeit('test_normal()', 'from __main__ import test_normal', number=10))
    # print("test_Thread", timeit('test_Thread()', 'from __main__ import test_Thread', number=10))
    print("test_Process", timeit('test_Process()', test_Process, number=10))
    def argument(a=1,b=2,c=3):
        print(a)
        print(b)
        print(c)
    argument(5, 6, c=7)

