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

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

y_value = np.random.randn(200)
x_value = np.arange(200)

ylim_min = y_value.min()-1
ylim_max = y_value.max()+1

yticks_min = y_value.min()+0.5
yticks_max = y_value.max()-0.5
ylim_setp = (yticks_max - yticks_min)/2.1

# xlim(min,max)和ylim(min,max)函数分别设置X轴和Y轴的刻度范围
plt.xlim(0,len(x_value))
plt.ylim(ylim_min,ylim_max)

# xticks(location,labels)和yticks(location,labels)函数分别设定X轴和Y轴的坐标标签。location为浮点数或整数组成的列表，
# 表示坐标轴上坐标的位置。labels为location等长的字符串列表，表示坐标的显示标签。
# Rotation参数可旋转调节坐标标签，当坐标密集时可避免标签重叠。
plt.xticks(np.arange(0, len(x_value), 20),
           ['2015-02-01', '2015-03-01', '2015-04-02', '2015-05-02',
            '2015-06-02', '2015-07-02', '2015-08-02', '2015-09-02',
            '2015-10-02', '2015-11-02'],rotation=45)
plt.yticks(np.arange(yticks_min, yticks_max, ylim_setp), [u'上限预警值', u'标准值', u'下限预警值'])

#注释(4)：title()函数添加标题，参数loc可调整标题显示的位置，分别为center、left、right
plt.title(u"函数式编程")#注释(4)

#注释(5)：xlabel()和ylabel()函数添加X轴、Y轴的显示标签
plt.xlabel(u"日期")#注释(5)
plt.ylabel(u"数值")#注释(5)

#注释(6)：grid(b=None, which='major', axis='both', **kwargs)函数增加并设定图形背景，便于更直观地读取线条中点的坐标取值及线条整体分布范围。参数b设定是否显示grid；参数which设定坐标轴分割线类型；参数axis制定绘制grid的坐标轴。
plt.grid(True)#注释(6)

#注释(7)：legend()函数增加图例显示，当多条曲线显示在同一张图中时，便于识别不同的曲线。参数loc用于设定图例在图中的显示位置，包括best（最适宜位置）、upper right（右上角）等。注：在绘制图形时需设定label，label值即为图例显示的文本内容。
plt.legend(loc='best')#注释(7)

#注释(8)：plot()函数用于绘制线条，linestyle参数设定线条类型，color参数指定线条的颜色，market参数设置数据点的形状，linewidth参数设定线条的宽度
plt.plot(x_value, y_value, label=u"随机误差", ls='-', c='r', lw=1) #注释(8)

plt.show()