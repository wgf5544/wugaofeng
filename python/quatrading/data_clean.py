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
    '''