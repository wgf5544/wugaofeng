'''
量化交易用户交互APP
'''


import wx
import wx.adv
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure


class Panel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent=parent, id=-1)

        # 通过Canvas对象嵌入Matplotlib的Figure
        self.figure = Figure()
        self.am = self.figure.add_subplot(1, 1, 1)
        self.figure_canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.topbox_sizer = wx.BoxSizer(wx.VERTICAL)
        self.topbox_sizer.Add(self.figure_canvas, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
        self.SetSizer(self.topbox_sizer)


class Frame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='量化软件', size=(1000, 600),
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)

        '''
        创建显示区面板
        显示Matplotlib绘制的图形。Matplotlib中底层的绘图操作由后端程序处理，
        后端会针对不同的输出选择在对应的界面显示图像或者以图像文件形式进行保存；
        此处后端输出为wxPython，将Matplotlib嵌入到wxPython的GUI界面中。
        
        canvas对象是真正进行绘图的后端，使程序逻辑上的绘图连接后端绘图程序在屏幕上绘制出来。
        '''
        self.disp_panel = Panel(self)

        '''
        创建参数区面板
        '''
        self.para_panel = wx.Panel(self, -1)
        _para_input_box = wx.StaticBox(self.para_panel, -1, '参数输入')
        _stock_name_combobox = ["浙大网新", "高鸿股份", "天威视讯", "北方导航"]
        # 股票名称复选框
        _stock_name_comb = wx.ComboBox(self.para_panel, -1, "浙大网新",
                                       choices=_stock_name_combobox,
                                       style=wx.CB_READONLY | wx.CB_DROPDOWN)
        stock_code_text = wx.StaticText(self.para_panel, -1, u'股票名称')

        # 创建日历控件选择数据周期
        # 结束时间
        self.dpc_end_time = wx.adv.DatePickerCtrl(self.para_panel, -1,
                                                  style=wx.adv.DP_DROPDOWN | wx.adv.DP_ALLOWNONE)
        # 起始时间
        self.dpc_start_time = wx.adv.DatePickerCtrl(self.para_panel, -1,
                                                    style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY
                                                          | wx.adv.DP_ALLOWNONE)

        _date_time_now = wx.DateTime.Now()  # wx.DateTime格式"03/03/18 00:00:00"
        self.dpc_end_time.SetValue(_date_time_now)
        self.dpc_start_time.SetValue(_date_time_now)
        _stock_data_text = wx.StaticText(self.para_panel, -1, u'日期(Start-End)')

        # 创建参数面板布局管理器
        _para_input_sizer = wx.StaticBoxSizer(_para_input_box, wx.VERTICAL)
        _para_input_sizer.Add(stock_code_text, proportion=0, flag=wx.EXPAND | wx.ALL, border=2)
        _para_input_sizer.Add(_stock_name_comb, 0, wx.EXPAND | wx.ALL | wx.CENTER, 2)
        _para_input_sizer.Add(_stock_data_text, proportion=0, flag=wx.EXPAND | wx.ALL, border=2)
        _para_input_sizer.Add(self.dpc_start_time, 0, wx.EXPAND | wx.ALL | wx.CENTER, 2)
        _para_input_sizer.Add(self.dpc_end_time, 0, wx.EXPAND | wx.ALL | wx.CENTER, 2)

        # 策略名称单选框
        _strategy_list = ["跳空缺口", "金叉\死叉", "N日突破", "均线突破"]

        self.strategy_input_box = wx.RadioBox(self.para_panel, -1, label='策略选取', choices=_strategy_list,
                                              majorDimension=4, style=wx.RA_SPECIFY_ROWS)
        # 交易信息提示框，多行|只读
        self.trade_text_ctrl = wx.TextCtrl(self.para_panel, -1, "交易信息提示:", style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 纵向box,proportion参数控制容器尺寸比例
        _vboxnet_sizer = wx.BoxSizer(wx.VERTICAL)
        _vboxnet_sizer.Add(_para_input_sizer, proportion=0, flag=wx.EXPAND | wx.BOTTOM, border=2)
        _vboxnet_sizer.Add(self.strategy_input_box, proportion=0, flag=wx.EXPAND | wx.BOTTOM, border=2)
        _vboxnet_sizer.Add(self.trade_text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        self.para_panel.SetSizer(_vboxnet_sizer)

        '''
        创建Right面板
        '''
        self.ctrl_panel = wx.Panel(self, -1)
        # 创建FlexGridSizer布局网格管理器
        self.flex_grid_sizer = wx.FlexGridSizer(rows=3, cols=1, vgap=3, hgap=3)

        # 实盘按钮
        self.firmoffer = wx.Button(self.ctrl_panel, -1, "实盘")
        # 选股按钮
        self.stockpick = wx.Button(self.ctrl_panel, -1, "选股")
        # 回测按钮
        self.backtrace = wx.Button(self.ctrl_panel, -1, "回测")

        # 加入Sizer中
        self.flex_grid_sizer.Add(self.firmoffer, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        self.flex_grid_sizer.Add(self.stockpick, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        self.flex_grid_sizer.Add(self.backtrace, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        self.flex_grid_sizer.SetFlexibleDirection(wx.BOTH)

        self.ctrl_panel.SetSizer(self.flex_grid_sizer)

        # 使用BoxSizer的布局管理器进行整体布局
        self.hbox_panel = wx.BoxSizer(wx.HORIZONTAL)

        self.hbox_panel.Add(self.para_panel, proportion=1, border=2, flag=wx.EXPAND | wx.ALL)

        self.hbox_panel.Add(self.disp_panel, proportion=4, border=2, flag=wx.EXPAND | wx.ALL)

        self.hbox_panel.Add(self.ctrl_panel, proportion=1, border=2, flag=wx.EXPAND | wx.ALL)

        self.SetSizer(self.hbox_panel)


class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    app = App()
    print('llllllll')
    app.MainLoop()