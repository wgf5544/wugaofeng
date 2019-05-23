__author__ = 'wgf'
__date__ = ' 下午11:54'

'''
量化交易系统中，绘图是数据可视化最直接的方法，也是直观分析数据必不可少的步骤。
Matplotlib是Python中专门用于数据可视化操作的第三方库，也是最流行的会图库。

两种绘图方式：函数式绘图和对象式绘图。
'''

# 函数式绘图
'''
MATLAB是数据绘图领域广泛使用的语言和工具，调用函数命令可以轻松绘图。、
Matplotlib是受NATLAB的启发而构建，设计了一套完全仿照MATLAB函数形式的绘图API。
'''
import matplotlib.pyplot as plt  # 导入Matplotlib库中的pyplot模块，该模块集合了类似MATLAB的绘图API
import numpy as np
import matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

y_value = np.random.randn(200)
x_value = np.arange(200)

ylim_min = y_value.min()-1
ylim_max = y_value.max()+1

yticks_min = y_value.min()+0.5
yticks_max = y_value.max()-0.5
ylim_setp = (yticks_max - yticks_min)/2.1

# xlim(min,max)和ylim(min,max)函数分别设置X轴和Y轴范围
plt.xlim(0, len(x_value))
plt.ylim(ylim_min, ylim_max)

# xticks(location,labels)和yticks(location,labels)函数分别设定X轴和Y轴的坐标标签。location为浮点数或整数组成的列表，
# 表示坐标轴上坐标的位置。labels为location等长的字符串列表，表示坐标的显示标签。
# Rotation参数可旋转调节坐标标签，当坐标密集时可避免标签重叠。
plt.xticks(np.arange(0, len(x_value), 20),
           ['2015-02-01', '2015-03-01', '2015-04-02', '2015-05-02',
            '2015-06-02', '2015-07-02', '2015-08-02', '2015-09-02',
            '2015-10-02', '2015-11-02'], rotation=45)
plt.yticks(np.arange(yticks_min, yticks_max, ylim_setp), [u'上限预警值', u'标准值', u'下限预警值'])

# title()函数添加标题，参数loc可调整标题显示的位置，分别为center、left、right
plt.title("函数式绘图")

# xlabel()和ylabel()函数添加X轴、Y轴的显示标签
plt.xlabel("日期")
plt.ylabel("数值")

# grid(b=None, which='major', axis='both', **kwargs)函数增加并设定图形背景，
# 便于更直观地读取线条中点的坐标取值及线条整体分布范围。参数b设定是否显示grid；参数which设定坐标轴分割线类型；
# 参数axis制定绘制grid的坐标轴。
plt.grid(True, which='both')

# legend()函数增加图例显示，当多条曲线显示在同一张图中时，便于识别不同的曲线。
# 参数loc用于设定图例在图中的显示位置，包括best（最适宜位置）、upper right（右上角）等。
# 注：在绘制图形时需设定label，label值即为图例显示的文本内容。
plt.legend(loc='best')

# plot()函数用于绘制线条，
# linestyle参数设定线条类型，
# color参数指定线条的颜色，
# markers参数设置数据点的形状，
# linewidth参数设定线条的宽度
# plt.plot(x_value, y_value, label="随机误差", ls='-', c='r', lw=1)

# plt.show()


# 对象式绘图
'''
引入Figure和FigureCanvas两个类，将绘图过程更改为面向对象式绘图。
Figure对象：整个图像为一个Figure对象，所有元素依附于Figure对象中。
Axes对象：Figure对象中可以包含一个或者多个Axes；每个Axes对象各自拥有坐标系统的绘图区域，
包含各自的Title（标题）、Axis（坐标轴）、Label（坐标轴标注）、Tick（刻度线）、Tick Label（刻度注释）等对象元素。

'''

from matplotlib.figure import Figure

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

y_value = np.random.randn(200)
x_value = np.arange(200)

ylim_min = y_value.min()-1
ylim_max = y_value.max()+1

yticks_min = y_value.min()+0.5
yticks_max = y_value.max()-0.5
ylim_setp = (yticks_max - yticks_min)/2.1

# pyplot模块中的figure()函数创建名为fig的Figure对象。
fig = plt.figure()

# 在Figure对象中创建两个Axes对象，每个Axes对象即为一个绘图区域。
'''
add_subplot()和add_axes()都返回一个matplotlib.axes.Axes对象。
add_subplot(211)：根据三个整数自动分配子区域在栅格的坐标位置。211表示2*1排第一个图像。
add_axes(rect)：表示图坐标[x0,y0,width,height]。(x0,y0)表示新区域左下角坐标，width和height表示宽和高。
plt.subplots(2,3)更为方便地创建Figure和subplot，在创建新的Figure时会同时返回一个含有已创建subplot对象的NumPy数组，
    可以对axes数组进行索引。sharex与sharey这两个参数来指定subplot共享x轴或y轴。
'''
ax1 = fig.add_subplot(211)
ax1.plot(x_value, y_value, label="随机误差", ls='-', c='r', lw=1)


'''
在Axes对象中增加坐标轴标签label对象、tick对象、ticklabel对象和标题title对象，也可以对坐标轴的取值范围xlim和ylim进行设定。
'''
# xlim(min,max)和ylim(min,max)函数分别设置X轴和Y轴的刻度线范围
ax1.set_xlim(0, len(x_value))
ax1.set_ylim(ylim_min, ylim_max)

# 分别设定X轴和Y轴的坐标标签。
ax1.set_xticks(np.arange(0, len(x_value), 20))
ax1.set_yticks(np.arange(yticks_min, yticks_max, ylim_setp))
ax1.set_xticklabels(['2015-02-01', '2015-03-01',
                     '2015-04-02', '2015-05-02',
                     '2015-06-02', '2015-07-02',
                     '2015-08-02', '2015-09-02',
                     '2015-10-02', '2015-11-02'],
                    fontsize='small')
ax1.set_yticklabels(['上限预警值', '标准值', '下限预警值'])
ax1.set_title("对象式绘图子图1")
# 设置坐标轴标注
ax1.set_xlabel("日期")
ax1.set_ylabel("数值")

ax2 = fig.add_subplot(222)  # 创建另一个Axes对象

ax2.plot(x_value, y_value, label="随机误差", ls='-', c='y', lw=1)

ax2.set_xlim(0, len(x_value))  # 调节X轴范围
ax2.set_ylim(ylim_min, ylim_max)  # 调节Y轴范围

# 调节刻度线范围
ax2.set_xticks(np.arange(0, len(x_value), 20))
ax2.set_yticks(np.arange(yticks_min, yticks_max, ylim_setp))
# 设置刻度线注释
ax2.set_xticklabels(['2015-02-01', '2015-03-01',
                     '2015-04-02', '2015-05-02',
                     '2015-06-02', '2015-07-02',
                     '2015-08-02', '2015-09-02',
                     '2015-10-02', '2015-11-02'],
                    rotation=45, fontsize='small')
ax2.set_yticklabels(['上限预警值', '标准值', '下限预警值'])

ax2.set_title("对象式绘图子图2")

# 设置坐标轴标注
ax2.set_xlabel(u"日期")
ax2.set_ylabel(u"数值")

# plt.show()

fig_ps, axes_ps = plt.subplots(2, 3)
print(fig_ps)
print(axes_ps)
for i in range(2):
    for j in range(3):
        axes_ps[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)

# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
line = ax.plot(x_value, y_value, label="随机误差", ls='-', c='r', lw=1)
print("line:", line)
print("ax.line:", ax.lines)
plt.show()


# 绘图机制分析
'''
Matplotlib中底层的绘图操作由后端程序处理，后端会针对不同的输出选择在对应的界面显示图像或者以图像文件形式进行保存；
后端输出包括PyGTK、wxPython、Tkinter、Qt4或者MacOS X等界面类的“互动后台”，以及PNG、SVG、PDF、PS等图像类的“非交互的后台”；
'''