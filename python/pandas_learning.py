__author__ = 'wgf'
__date__ = ' 下午1:41'
import datetime

import numpy as np
import pandas as pd

'''
Pandas是Python环境下最有名的数据统计包，是基于Numpy的含有更高级数据结构和工具的数据分析包。
Series和DataFrame是Pandas核心数据结构。

'''

# Series数据生成和访问

'''
Series类似于一维数组对象，由一组数据和相对应的一组索引组成。
    
    基本方法：s = pd.Series(data, index=index)，data可以是list、ndarray的阵列组成的一维数组，也可以是字典、常量值组成的一维数组。


'''


# 以列表作为数据类型创建一个Series对象，左边是索引index，右边是值values。value中包含多种基本类型的值，dtype为object
s = pd.Series([-1.55666192, -3j+2.1, 1, -1.37775038, 'ss'],
              index=['a', 'b', 'c', 'd', 'e'])
print(s)

# s = pd.Series([-1.55666192, -0.75414753, 0.47251231, -1.37775038, -1.64899442],
#               index=['a', 'b', 'c', 'd', 'e'], dtype='int8')


# 以字典作为数据类型创建一个Series对象
s = pd.Series({'a': 0., 'b': 1., 'c': 2.}, index=['b', 'c', 'd', 'a'])
print(s)
print('===========')
print(s.index)
print(s.values)
print(s['a'])
print(s[['a', 'b']])
print('==========')
print(s[:2])
print(s[['a']])



# DataFrame数据生成和访问
'''
DataFrame是一个表格型的数据结构，既有行索引也有列索引；

创建DataFrame的方法：df = pd.DataFrame(data, index=index,columns=columns)，
data参数可以是列表、一维ndarray或Series组成的字典、字典组成的字典、二维的ndarray。
可以看成是共享同一个index的Series的集合。是一个二维的数据结构。




'''

# 以列表组成的字典形式创建DataFrame，每个键对应一个列
df = pd.DataFrame({'one': [1., 2., 3., 5], 'two': [1., 2., 3., 4.]})
print(df)

# 以嵌套列表形式创建DataFrame
df = pd.DataFrame([[1., 2., 3., 5],[1., 2., 3., 4.]],
                  index=['a', 'b'], columns=['one', 'two', 'three', 'four'])
print(df)


# 创建一个二维ndarray阵列,并指定散列的类型分别为整数、浮点、字符串
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
print('-------------')
print(data)

# 以整数、浮点和字符串类型对data进行赋值
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
print(data)
# 二维ndarray形式创建DataFrame
df = pd.DataFrame(data)
print(df)

# 指定行索引为['first', 'second']，没有指定行索引，会自动创建整数型行索引
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

# 指定列索引columns
df = pd.DataFrame(data, columns=['C', 'A', 'B'])
print(df)


# 创建一组以Series组成的字典
data = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
        'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# 以Series组成的字典形式创建DataFrame
df = pd.DataFrame(data)
print(df)


# 创建一组字典的列表数据
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# 字典的列表创建DataFrame
df = pd.DataFrame(data2)
print(df)


# DataFrame数据对象的访
print('df 数据对象访问-----------------')
data = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
        'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# 以Series组成的字典形式创建DataFrame
df = pd.DataFrame(data)
print(df.index)
print(df.columns)
print(df.values)

# 访问某一行
print('--------------------')
print(df[0:1])
print('--------------------')
print(df[1:1])
print('--------------------')
print(df[0:2])

# 访问某一列
print('--------------------')
print(df['one'])
print(df.one)

# loc 通过索引标签来访问,行标签或列标签
print('-----loc--------')
print(df.loc['a'])


print(df.loc[:, ['one', 'two']])

print(df.loc[['a', ], :])


# iloc 通过位置来选取元素，选择指定行或列（非连续）时需要用"[]"括起来

print(df.iloc[0:2,0:1] )


print(df.iloc[0:2] )

print(df.iloc[[0,2],[0,1]])


# ix 结合位置iloc和标签loc来选取元素。
print('------ix----------')

print(df.ix['a'])

print(df.ix['a',['one','two']])

print(df.ix['a',[0,1]])

print(df.ix[['a','b'],[0,1]])
print(df.ix[[0,1],['one','two']])




'''
CSV文件的加载和存储

Pandas库提供了用于将表格型数据读取为DataFrame对象的方法；
read_csv可支持从文件、url、文件型对象中加载带分隔符（默认为逗号）的数据；
to_csv方法将DataFrame数据以逗号分隔方式存储于CSV格式文件中。

'''


# =============加载CSV文件=========
print('==============加载CSV文件=========')
'''
CSV即逗号分隔值（Comma-Separated Values，或称字符分隔值）单元格中包含逗号，那么这个单元格中的内容以双引号引注。
'''
'''
header参数指定数据开始的行数作为列名;
index_col参数指定数据中哪一列作为Dataframe的行索引;
parse_dates=True，指把行索引字符串解析成时间格式;
encoding参数指定unicode文本编码的格式；

'''
df_csvload = pd.read_csv('/Users/wgf/git_repository/wugaofeng/python/csv/table_stock',
                          parse_dates=True, index_col=0, encoding='gb2312')
print(df_csvload.index)

# 存储CSV文件============
print('==============存储CSV文件============')
df_csvload = pd.read_csv('/Users/wgf/git_repository/wugaofeng/python/csv/table_stock',
                          parse_dates=True, index_col=0, encoding='gb2312')
# 扩充2个交易日的股票数据
df_adddat = pd.DataFrame([{u'Open': 1.1, u'High': 1.2, u'Low': 1.3, u'Close': 1.4},
                          {u'Open': 2.1, u'High': 2.2, u'Low': 2.3, u'Close': 2.4}],
                         index=[datetime.datetime.strptime("2016-06-25 00:00:00", "%Y-%m-%d %H:%M:%S"),
                                datetime.datetime.strptime("2016-06-26 00:00:00", "%Y-%m-%d %H:%M:%S")])
df_csvload = df_csvload.append(df_adddat)

# 存储csv文件数据
df_csvload.to_csv('/Users/wgf/git_repository/wugaofeng/python/csv/table_stock',
                  columns=df_csvload.columns, index=True)




