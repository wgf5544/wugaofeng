'''

Args:
Returns:
'''
import pandas as pd
from pandas import DataFrame


def view_info(df: DataFrame) -> str:
    """
    查看数据信息
    :param df:
    :return:
    """
    if isinstance(df, DataFrame):
        _head = df.head()  # 前5行数据
        _tail = df.tail()  # 后5行数据
        _columns = df.columns  # 查看列名
        _index = df.index  # 查看索引
        _shape = df.shape  # 查看形状
        _describe = df.describe()  # 查看各列数据描述性统计
        _df_info = df.info()  # 查看缺失及每列数据类型

        result = f"{'='*10}前5行数据{'='*10}\n{_head}\n\n" \
            f"{'='*10}后5行数据{'='*10}\n{_tail}\n\n" \
            f"{'='*10}查看列名{'='*10}\n{_columns}\n\n" \
            f"{'='*10}查看索引{'='*10}\n{_index}\n\n" \
            f"{'='*10}查看形状{'='*10}\n{_shape}\n\n" \
            f"{'='*10}查看各列数据描述性统计{'='*10}\n{_describe}\n\n" \
            f"{'='*10}查看缺失及每列数据类型{'='*10}\n{_df_info}\n\n"

        print("sssss", _df_info)

        return result
    else:
        raise TypeError("df's type  is not DataFrame!")

    return None


if __name__ == "__main__":
    df_csvload = pd.read_csv('../csv/table_stock', parse_dates=True, index_col=0, encoding='gb2312')
    # 数据信息查看
    df_info = view_info(df_csvload)
    print(df_info)

    """
    缺失值处理
    数据有可能出现一些缺失值NaN(NOT a NUMBER)
    """
    print(df_csvload.isnull())  # 缺失为True
    print(df_csvload.notnull())  # 缺失为False
    print("--------------------")

    # 查找缺失值所在的行
    print(df_csvload[df_csvload.isnull().T.any().T])  # .any()筛选满足True值条件列方法,查找出含有NaN的行。

    # 缺失值删除
    '''
    axis=0表示删除行，=1表示删除列；how='any'表示只要有一个缺失值就删除,='all'表示当只有所有值为缺失值才删除。
    '''

    df_csvload_del = df_csvload.dropna(axis=0, how='any')
    print(df_csvload_del)
    # 缺失值填充
    '''
    method是填充方式，='ffill'表示用行或列上一个值来填充缺失值，='bfill'表示用下一个值来填充，inplace=True表示原地修改。
    axis=0表示列，=1表示行。
    '''
    df_csvload.fillna(method='bfill', axis=0, inplace=True)
    print('填充缺失值-------------------------------------')
    print(df_csvload)
    print(df_csvload[df_csvload.isnull().values == True])  # 查看删除和填充缺失值后的值

    '''
    特殊值处理
    浮点数精度转换，'{:0.2f}'.format(312.8845)保留两位小数点，
    
    applymap()方法在不使用元素级方法的情况下自定义lambda方法作用于DataFrame元素级，对所有数据起作用,
    但是转化后数据为字符串str，推荐使用round()。
    
    astype()强制类型转换。
    
    使用&、|、==这些符号df数据实现条件筛选查看所有0值的元素
    '''
    # df_csvload = df_csvload.applymap(lambda x: '{:.2f}'.format(x))
    # print(df_csvload)
    df_csvload = df_csvload.round(2)
    print(df_csvload)
    print(df_csvload.info())

    print(df_csvload.values == 0)
    print(df_csvload[df_csvload.values == 0])

    df_csvload.loc[df_csvload.loc[:, "Low"] == 0 , 'Low']=df_csvload.Low.median() # 用'Low'列的中位值替换
    print(df_csvload.loc['2018-01-15'])


    '''
    数据运算转化
    
    获知股票数据每天的最高价、最低价、开盘价和收盘价，从而得到价格震荡幅度。
    震荡幅度在一定程度上可以体现股票的活跃程度，振幅较小说明不够活跃，振幅较大说明比较活跃。
    
    振幅的计算公式：(最高价-最低价)/昨日收盘价，
    “2018-01-02”缺失前一天的收盘价，导致当天计算的振幅值为NaN，此处用多个交易日的平均振幅替换
    
    shift()移动函数，shift(periods=1, freq=None, axis=0)，periods表示移动步数，正数向下或者向左，负数表示向相反方向移动；
    axis=0表示行的方向，上下移动，=1表示列的方向，左右移动。
    '''
    change = df_csvload.High -df_csvload.Low
    print(change)
    df_csvload['pct_change'] = (change/df_csvload.Close.shift(1)) # shi{}
    print(df_csvload)

    df_csvload['pct_change'].fillna(df_csvload['pct_change'].mean(), inplace=True)  # 用多个交易日的平均振幅值替换
    print(df_csvload)


    '''
    数据合并和链接
    三种方式：
    pandas.merge:
    pandas.concat:沿着一个轴，水平连接扩展。
    combine_first:
    
    '''
    dfv_csvload = pd.read_csv('../csv/volume_stock', parse_dates=True, index_col=0,
                              encoding='gb2312')
    print(dfv_csvload)

    df_concat = pd.concat([df_csvload, dfv_csvload], axis=1, keys=['Price', 'amount'])
    print(df_concat)