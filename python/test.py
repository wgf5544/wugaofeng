__author__ = 'wgf'
__date__ = ' 下午10:39'

import requests
import json

febg_msg = {
    "name": "name",
    "parent_group_id": 0,
    "remark": "remark",
    "surveillance_mode": 0,
    "id": -1,
    "children_group_id": "",
    "sensorId": "Lux0001"

}


class aaa(object):
    def __init__(self, name: str = 'zhangsan'):
        print(name)

    def __bool__(self):
        return False

    def __repr__(self):
        return 'aaaaaaaa'


if __name__ == "__main__":
    #
    # url = "http://192.168.11.224:12000/febg/v1/sensor_group"
    # try:
    #     r = requests.put(url, data=json.dumps(febg_msg), timeout=3)
    #     print(r.text)
    # except Exception as e:
    #     print(e)
    #
    # print(range(10))



    # print(x**2 for x in range(5))

    a = aaa()
    print(bool(a))

    print(333//31)

    print(sum(map(int, str(2 ** 1000))))
    print(2**1000)