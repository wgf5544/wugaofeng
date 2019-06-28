
'''

Args:
Returns:
'''
import requests
import unittest

class RequestsTestSuite(unittest.TestCase):
    """Requests test cases."""

    def setUp(self):
        print("开始")
        pass

    def tearDown(self):
        """Teardown."""
        print("销毁")
        pass

    def test_invalid_url(self):
        self.assertRaises(Exception, requests.get, '2')

    def test_HTTP_200_OK_GET(self):
        r = requests.get('http://google.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTPS_200_OK_GET(self):
        r = requests.get('https://google.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTP_200_OK_HEAD(self):
        r = requests.head('http://google.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTPS_200_OK_HEAD(self):
        r = requests.head('https://google.com')
        self.assertEqual(r.status_code, 200)

    def test_AUTH_HTTPS_200_OK_GET(self):
        auth = requests.AuthObject('requeststest', 'requeststest')
        url = 'https://convore.com/api/account/verify.json'
        r = requests.get(url, auth=auth)

        self.assertEqual(r.status_code, 200)


# if __name__ == "__main__":
#     print("开始测试。。。。。。")
#     req = RequestsTestSuite()
#     req.test_invalid_url()

__author__ = 'wgf'
__date__ = ' 下午10:08'
import requests

import requests
s = requests.Session()
r = s.get('https://httpbin.org/get')
print(r)
dict()

