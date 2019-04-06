#什么是迭代协议
#用for能遍历的对象是可迭代对象（Iterable），是实现了 __iter__。
#list等[]能下标方式访问是实现了__getitem__ ;能用于for循环遍历是实现了__iter__.是可迭代对象。但不是迭代器。
#迭代器是什么？ 迭代器（Iterator）是访问集合内元素的一种方式， 一般用来遍历数据
#迭代器和以下标的访问方式不一样， 迭代器是不能返回的, 迭代器惰性的可迭代对象（实现了__iter__），在next()访问的时候才会计算生成数据(实现了__next__)。
#

from collections.abc import Iterable, Iterator
a = [1,2]
iter_rator = iter(a)
#print (isinstance(a, Iterable))
#print (isinstance(iter_rator, Iterator))

print(isinstance(iter(1),Iterator))
str
