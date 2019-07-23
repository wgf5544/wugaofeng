__author__ = 'wgf'
__date__ = ' 下午11:24'


import copy
a = 'ss'*2
b = 'ss'*2

# a[1].append(3)
print(a)
print(b)


# assert id(a) == id(b)
print(id(a),' ', id(b))
import  copy
##  浅拷贝
lst = [1, 2,3,4,[1,2]]
lst1 = lst[:]           #从头切到尾,重新完整的复制了一份
# lst1 = lst.copy()
# lst1 = copy.copy(lst)
print(id(lst),id(lst1))

## 深拷贝
import copy
lst = [1,2,[3,4],5]
lst2 = copy.deepcopy(lst)       #copy.deepcopy 深拷贝
print(id(lst1[2]),id(lst[2]))  #肯定不一样d's

# 1.赋值没有创建新对象,多个变量共享一个内容

# 2.浅拷贝,会创建新对象,新对象里面的内容不会被拷贝

# 3.深拷贝,创建一个一摸一样完全新的对象 不可变对象,还是原来的,可变对象创建新的

import random

rand = random.random()*100
for i in range(100):
    print(int(random.random()*100%100))

