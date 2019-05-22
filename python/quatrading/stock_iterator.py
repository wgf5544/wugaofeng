'''

Args:
Returns:
'''

import pandas as pd
df_csvload = pd.read_csv('../csv/table_stock', parse_dates=True, index_col=0, encoding='gb2312')


'''
for... in  循环迭代方法
'''


def iterator_looping(df):
    disftance_list = []
    for i in range(0,len(df)):
        disftance_list.append(df.iloc[i]['Open']-df.iloc[i]['Close'])
    return disftance_list


print(iterator_looping(df_csvload))


'''
iterrows() 生成器方式
实现生成器方式：生成器函数（yield）；生成器生成式。
'''

def iterrows_loopiter(df):
    disftance_list = []
    for index, row in df.iterrows():
        disftance_list.append(row['Open']-row['Close'])
    return disftance_list

print(iterrows_loopiter(df_csvload))


'''
apply() 循环方式
apply()方法可将函数应用于DataFrame特定行或列。按照行或者列的方式循环。
函数由lambda方式在代码中内嵌实现，lambda函数的末尾包含axis参数，用来告知Pandas将函数运用于行（axis = 1）或者列（axis = 0）
'''

disftance_list = df_csvload.apply(lambda row: (row['Open']-row['Close']), axis=1)
print(disftance_list)


'''
矢量化遍历方式
矢量化方式可使用Pandas series的矢量化方式和NumPy array矢量化方式两种。
Pandas的DataFrame、series基础单元数据结构基于链表，因此可将函数在整个链表上进行矢量化操作，而不用顺序执行每个值。
Pandas提供非常丰富的矢量化函数库，我们可把整个series作为参数传递，对整个链表进行计算。
'''
df_csvload['rate'] = df_csvload['Open']-df_csvload['Close']
print(df_csvload['rate'])



'''
执行效率比较

循环执行效率最慢。
iterrows有所提升，针对DataFrame进行了优化。
apply行循环有所提升。
Pandas Series矢量化运算更快，但有类型、索引等操作的开销。
Numpy arrays矢量化运算速度最快，使用预编译的C代码在底层进行优化。

'''

# 使用timeit方法对比方法参考例程如下，需要import timeit模块
from timeit import timeit

def test1():
    iterator_looping(df_csvload)


def test2():
    iterrows_loopiter(df_csvload)


def test3():
    disftance_list = df_csvload.apply(lambda row: (row['Open']-row['Close']), axis =1)


def test4():
    df_csvload['rate'] = df_csvload['Open']-df_csvload['Close']


def test5():
    df_csvload['rate'] = df_csvload['Open'].values-df_csvload['Close'].values


# for...in循环迭代方式
t1 = timeit('test1()', 'from __main__ import test1', number=1000)
# iterrows()遍历方式
t2 = timeit('test2()', 'from __main__ import test2', number=1000)
# apply()方法循环方式
t3 = timeit('test3()', 'from __main__ import test3', number=1000)
# Pandas series的矢量化方式
t4 = timeit('test4()', 'from __main__ import test4', number=1000)
# NumPy arrays的矢量化方式：
t5 = timeit('test5()', 'from __main__ import test5', number=1000)

print(f"loop:{t1}")
print(f'iterrows:{t2}')
print(f'apply:{t3}')
print(f'Pandas Series:{t4}')
print(f'NumPy array:{t5}')