__author__ = 'wgf'
__date__ = ' 下午10:39'

import requests
import json
from timeit import timeit

febg_msg = {
    "name": "name",
    "parent_group_id": 0,
    "remark": "remark",
    "surveillance_mode": 0,
    "id": -1,
    "children_group_id": "",
    "sensorId": "Lux0001"

}
def time1():
    return 888999777 % 2
def time2():
    return 888999777 & 1

def trydemo():
    try:
        print('1111')

    except Exception as e:
        print(e)
    else:
        print('2222')

def fordemo():
    for i in range(10):
        if i == 5:
            print(i)
            continue
    else:
        print('===5')


class Student():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

if __name__ == "__main__":

    # url = "http://192.168.11.224:12000/febg/v1/sensor_group"
    # try:
    #     r = requests.put(url, data=json.dumps(febg_msg), timeout=3)
    #     print(r.text)
    # except Exception as e:
    #     print(e)
    #
    # print(range(10))
    #
    #
    # print(list(x**2 for x in range(5)))
    # print(888999&1)
    # t1 = timeit("time1()", 'from __main__ import time1', number=10)
    # t2 = timeit("time2() ", 'from __main__ import time2', number=10)
    # print(t1,' ',t2)

    x = 1000
    y = 2000

    x = x ^ y
    y = x ^ y
    x = x ^ y

    # print(f'x:{x}, y:{y}')
    #
    # m =2
    # n = 3
    # p = m^n
    # print(True or False and True)
    # a = [3,5,'3',0]
    # print(all(a))
    #
    # trydemo()
    # s = Student('1')
    # s1 = Student('1')
    # print(s is s1)
    # # ==比较的是值；is 比较是地址id()
    # a = None
    # print(a is None)
    # info = 'sensor_ubuntu_2.1.21.0.tgz'
    # s = info.split('.')
    # print('.'.join(info.split('.')[:-1]))
    # sensor_version = s[-1].split()
    # print(True or False and False)
    #
    # print('ssbbcc'.count('bc'))
    # print( float("inf"))

    import bisect
    import time

    # BREAKPOINTS 必须是已经排好序的，不然无法进行二分查找
    BREAKPOINTS = (1, 60, 3600, 3600 * 24)
    TMPLS = (
        # unit, template
        (1, "less than 1 second ago"),
        (1, "{units} seconds ago"),
        (60, "{units} minutes ago"),
        (3600, "{units} hours ago"),
        (3600 * 24, "{units} days ago"),
    )


    def from_now(ts):
        """接收一个过去的时间戳，返回距离当前时间的相对时间文字描述
        """
        seconds_delta = int(time.time() - ts)
        unit, tmpl = TMPLS[bisect.bisect(BREAKPOINTS, seconds_delta)]
        print(bisect.bisect(BREAKPOINTS, seconds_delta))
        return tmpl.format(units=seconds_delta // unit)

    now = time.time()
    print(from_now(now - 24))
    print()

    a = {'s':'sdfghjkliuyt','ss':'ssssss'}
    a['s'][100:200]
    ret = a.pop('s1',1111)
    print(ret)
    print(a)
    numbers = [3, 7, 8 , 2, 21]
    print(next((i for i in numbers if i % 2 == 0)))

    # 在 Python 3.6 中，默认的字典类型修改了实现方式，已经变成有序的了
    l = [10, 2, 3, 21, 10, 3]
    from collections import OrderedDict
    ss = list(OrderedDict.fromkeys(l).keys())
    dict_cc = OrderedDict.fromkeys(l)
    dict_cc[10] = 111
    print(dict_cc)
    a = dict()

    import sys
    print('...:', sys.getrecursionlimit())

    s = input()
    print(s)