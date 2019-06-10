from typing import Optional, Awaitable

from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import socket
import tornado
import functools
import time
from tornado.concurrent import Future
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
requst_set = set()
start_times = 0
first = False


class BaseHandler(RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

    def _response(self, response):

        if response:
            self.write(response)
        else:
            self.write(b"222")
            self.set_status(201)

        self.flush()  # 将缓冲区刷新到网络
        self.finish()  # 关闭长连接

    def on_connection_close(self) -> None:
        '''
        未收完服务端返回，客户端关闭连接时调用，此时服务已经发送数据。
        '''
        super().on_connection_close()
        print("client closed connection")

    def prepare(self) -> Optional[Awaitable[None]]:
        '''
        在执行request method（post/get..）之前调用
        '''
        print(f"received request，and request info :{repr(self.request)}")
        return super().prepare()

    def on_finish(self):
        '''
        服务端发送完数据时调用，此处可做一些清理工作
        '''
        print(f"the response has been sent to the client, request info :{str(self.request)}")



class IndexHandler(RequestHandler):

    def get(self):
        self.write("<a href='"+self.reverse_url("login")+"'>用户登录</a>")


class RegistHandler(RequestHandler):
    def initialize(self, title):
        self.title = title

    def get(self):
        self.write("注册业务处理:" + str(self.title))


class LoginHandler(BaseHandler):

    executor = ThreadPoolExecutor(10)

    @gen.coroutine
    def post(self):

        body = self.request.body

        result = yield self.handle(body)

        self._response(result)

        print(time.time()-start_times)

    @run_on_executor
    def handle(self,body):

        try:
            # todo:to do something
            print(body)
            time.sleep(1)
            1/0
        except Exception as e:
            return None
        return 'non-bloacking'


if __name__ == "__main__":
    app = Application(
        [
            (r"/heartbeat", IndexHandler),
            (r"/register", RegistHandler, {"title": "会员注册"}),
            (r"/log", LoginHandler),
        ]
    )

    # http_server = HTTPServer(app)
    # http_server.listen(8000)
    #
    # IOLoop.current().start()

    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # sock.setblocking(0)  # 把监听的socket设置成非阻塞
    print(app)
    sockets = tornado.netutil.bind_sockets(port=8000, address='127.0.0.1', reuse_port=True)
    tornado.process.fork_processes(1)
    server = tornado.httpserver.HTTPServer(app)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()