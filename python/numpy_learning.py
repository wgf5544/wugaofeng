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
print('type : {}'.format(n.dtype))
print('shape : {}'.format(n.shape))
print('strides : {}'.format(n.strides))


# 测试Numpy数组和等价的Python列表性能差距


my_arr = np.arange(1000000)

my_list = list(range(1000000))

# try:
#     t1 = timeit('for _ in range(10): my_arr2 = my_arr * 2', 'from __main __ import my_arr', number=1)
#     t2 = timeit('for _ in range(10): my_list2 = [x * 2 for x in my_list]', 'from __main__ import my_list', number=1)
# except Exception as e:
#     print(e)
#     traceback.print_exc()

# print(t1, ' ', t2)


# NumPy 矢量特性和广播特性
'''
矢量特性：对数组的进行复杂运算时，可以仅仅使用简洁表达式代替Python的for循环做法。也就是并行化运算。
    矢量化数组运算要比纯Python快上一两个数量级。
    大小相等的数组之间，任何算术运算都会应用到元素级别。

广播机制：为不同大小数组之间的运算提供的一种处理机制。
    NumPy的广播机制放宽了数组形状的限制，使得较小形状的数组"广播"到较大数组相同形状尺度上进行对等数学计算。
    
    广播原则（数组兼容性）：两个数组操作时，从后面的维度向前执行，只有当它们相等，或者其中一个为1时，两个维度才算是兼容的，
    否则会抛出错误表示两个阵列形状不兼容。相兼容的两数组计算后结果与各维度最大尺寸相等。
    
    
    
'''

x = np.ones((4, 3))
print(x)

y = np.ones((1, 4, 1))

print(y)

xy = x+y
print('计算结果：{} , 形状：{}'.format(xy, xy.shape))
print(np.sqrt(xy))
print(np.exp(xy))
print(np.std(xy))
print(np.min(xy))
print(np.max(xy))

# 索引选取数据
'''
常用NumPy方法：
    元素级数组函数：计算各元素平方根np.sqrt()、计算各元素指数np.exp()返回自然常数e（2.71828）的n次方。
    基本的数据统计方法：标准差std()、max()、min()
    
    data[] 中通过表达式符号“==”、“!=”、“&”、“|”以矢量化方式选取我们想要的数据，
    其实表达式将会产生一个布尔型数组，用这个布尔型数组数组索引。
'''

data = np.random.randn(3, 4)
print(data)
data1 = data[[True, False, False],1]
print(data1)
print(data < 0)