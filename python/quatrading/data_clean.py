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

"""
缺失值处理
数据有可能出现一些缺失值NaN(NOT a NUMBER)
"""
if __name__ == "__main__":
    df_csvload = pd.read_csv('../csv/table_stock', parse_dates=True, index_col=0, encoding='gb2312')
    # 数据信息查看
    df_info = view_info(df_csvload)
    print(df_info)
    print(df_csvload.isnull())
