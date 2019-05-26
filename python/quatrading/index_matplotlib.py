'''
技术分析常用指标绘制
目前常用的技术分析指标有K线图、均线、MACD、KDJ等，
其实所有的技术指标都是依据股票收盘价、开盘价、最高价、最低价、成交价等原始的交易数据用特定的算法公式计算而来的。
'''
import matplotlib.gridspec as gridspec  # 新增导入gridspec用于分割子图
import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np

import crawl_data

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# ig = plt.figure(figsize=(8, 6), dpi=100, facecolor="white")  # 创建fig对象
# fig.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

df_stockload = crawl_data.crawl("600797.SS", "yahoo", year=2018)

# 创建子图
# graph_KAV = fig.add_subplot(1, 1, 1)
# graph_KAV.set_title(u"600797 浙大网新-日K线")
#
# graph_KAV.set_xlabel(u"日期")
#
# graph_KAV.set_ylabel(u"价格")
#
# graph_KAV.set_xlim(0, len(df_stockload.index))  # 设置一下x轴的范围
#
# graph_KAV.set_xticks(range(0, len(df_stockload.index), 15))  # X轴刻度设定，每15天标一个日期
#
# graph_KAV.grid(True, color='k')
#
# graph_KAV.set_xticklabels(
#     [df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_KAV.get_xticks()])  # 标签设置为日期
# # X轴每个ticker标签都向右倾斜45度
#
# for label in graph_KAV.xaxis.get_ticklabels():
#     label.set_rotation(45)
#
#     label.set_fontsize(10)  # 设置标签字号


# # k线图可视化
# def ochl():
#
#     # 绘制K线走势
#     mpf.candlestick2_ochl(graph_KAV, df_stockload.Open, df_stockload.Close, df_stockload.High, df_stockload.Low,
#                           width=0.5, colorup='r', colordown='g')
#
#     plt.show()
#
#
# # 均线可视化 pandas.rolling.mean()
# def mean_line():
#     """ 绘制移动平均线图 """
#
#     df_stockload['Ma20'] = df_stockload.Close.rolling(window=20).mean()  # pd.rolling_mean(df_stockload.Close,window=20)
#
#     df_stockload['Ma30'] = df_stockload.Close.rolling(window=30).mean()  # pd.rolling_mean(df_stockload.Close,window=30)
#
#     df_stockload['Ma60'] = df_stockload.Close.rolling(window=60).mean()  # pd.rolling_mean(df_stockload.Close,window=60)
#
#     numt = np.arange(0, len(df_stockload.index))
#     print(df_stockload.Ma20)
#     # 绘制均线走势
#
#     graph_KAV.plot(numt, df_stockload['Ma20'], 'black', label='M20', lw=1.0)
#
#     graph_KAV.plot(numt, df_stockload['Ma30'], 'green', label='M30', lw=1.0)
#
#     graph_KAV.plot(numt, df_stockload['Ma60'], 'blue', label='M60', lw=1.0)
#
#     graph_KAV.legend(loc='best')
#     plt.show()

# 绘制成交量图
def volumn():
    fig = plt.figure(figsize=(8, 6), dpi=100, facecolor="white")  # 创建fig对象
    gs = gridspec.GridSpec(2, 1, left=0.05, bottom=0.15, right=0.96, top=0.96, wspace=None, hspace=0,
                           height_ratios=[3.5, 1])
    numt = np.arange(0, len(df_stockload.index))
    graph_KAV = fig.add_subplot(gs[0, :])
    graph_KAV.set_title(u"600797 浙大网新-日K线")

    graph_KAV.set_xlabel(u"日期")

    graph_KAV.set_ylabel(u"价格")

    graph_KAV.set_xlim(0, len(df_stockload.index))  # 设置一下x轴的范围

    graph_KAV.set_xticks(range(0, len(df_stockload.index), 15))  # X轴刻度设定，每15天标一个日期

    graph_KAV.grid(True, color='k')

    graph_KAV.set_xticklabels(
        [df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_KAV.get_xticks()])  # 标签设置为日期

    # 绘制K线走势
    mpf.candlestick2_ochl(graph_KAV, df_stockload.Open, df_stockload.Close, df_stockload.High, df_stockload.Low,
                              width=0.5, colorup='r', colordown='g')

    graph_VOL = fig.add_subplot(gs[1, :])
    graph_VOL.bar(numt, df_stockload.Volume,
                  color=['g' if df_stockload.Open[x] > df_stockload.Close[x] else 'r' for x in
                         range(0, len(df_stockload.index))])

    graph_VOL.set_ylabel(u"成交量")

    graph_VOL.set_xlabel(u"日期")

    graph_VOL.set_xlim(0, len(df_stockload.index))  # 设置一下X轴的范围

    graph_VOL.set_xticks(range(0, len(df_stockload.index), 15))  # X轴刻度设定，每15天标一个日期

    graph_VOL.set_xticklabels(
        [df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_VOL.get_xticks()])  # 标签设置为日期

    # 将日K线X轴labels隐藏
    for label in graph_KAV.xaxis.get_ticklabels():
        label.set_visible(False)

    # X轴每个ticker标签都向右倾斜45度
    for label in graph_VOL.xaxis.get_ticklabels():

        label.set_rotation(45)

        label.set_fontsize(10) #设置标签字号

    plt.show()

if __name__ == '__main__':
    # ochl()
    # mean_line()
    volumn()