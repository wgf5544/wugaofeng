__author__ = 'wgf'
__date__ = ' 下午10:08'
import requests

import requests
s = requests.Session()
r = s.get('https://httpbin.org/get')
print(r)
dict()