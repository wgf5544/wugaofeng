__author__ = 'wgf'
__date__ = ' 下午10:18'

import timeit
import traceback

import numpy as np

"""
NumPy(numerical python)是python数值计算最重要的基础数据包，
大多数提供科学计算的包都是以NumPy数组为基础构建的，比如Pandas数据统计包。

NumPy的核心是N维数组对象ndarray，它是一个具有矢量算术运算和复杂广播能力、快速且节省空间的多维数组。
"""

# 高效处理能力，基于ndarray处理数据的机制
'''
ndarray的内部组成：
    一个指向数据（内存中的数据块）的指针；
    一个描述数据在数组中存储大小的数据类型dtype；
    一个表示数组形状大小的shape元组；
    一个字节数跨度元组strides；
C语言编写的算法库可以直接操作内存，相比python的内置序列，无需进行类型检查和其他前期工作，使用内存也会更少。

    


'''
n = np.ones((4, 5))
print(n)
print(n.dtype)
print(n.shape)
print(n.strides)


# 测试Numpy数组和等价的Python列表性能差距


my_arr = np.arange(1000000)

my_list = list(range(1000000))

try:
    t1 = timeit('for _ in range(10): my_arr2 = my_arr * 2', 'from __main __ import my_arr', number=1)
    t2 = timeit('for _ in range(10): my_list2 = [x * 2 for x in my_list]', 'from __main__ import my_list', number=1)
except Exception as e:
    print(e)
    traceback.print_exc()

# print(t1, ' ', t2)