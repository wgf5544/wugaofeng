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
if __name__ == "__main__":

    url = "http://192.168.11.224:12000/febg/v1/sensor_group"
    try:
        r = requests.put(url, data=json.dumps(febg_msg), timeout=3)
        print(r.text)
    except Exception as e:
        print(e)

    print(range(10))


    print(list(x**2 for x in range(5)))