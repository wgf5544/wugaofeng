

# !/usr/bin/env python
# -*- coding:utf-8 -*-


import tornado.web
from tornado import gen
from tornado import httpclient


# 方式一：
class AsyncHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self, *args, **kwargs):
        print('进入')
        http = httpclient.AsyncHTTPClient()
        data = yield http.fetch("http://127.0.0.1:8000/log", body={22:44})
        print('完事', data)
        self.finish('6666')


# 方式二：
# class AsyncHandler(tornado.web.RequestHandler):
#     @gen.coroutine
#     def get(self):
#         print('进入')
#         http = httpclient.AsyncHTTPClient()
#         yield http.fetch("http://www.google.com", self.done)
#
#     def done(self, response):
#         print('完事')
#         self.finish('666')


application = tornado.web.Application([
    (r"/async", AsyncHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
