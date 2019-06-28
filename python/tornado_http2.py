from typing import Optional, Awaitable

from tornado.web import Application, RequestHandler, url,stream_request_body
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
from tornado.platform.asyncio import AsyncIOMainLoop
# from aiokafka import AIOKafkaProducer
import asyncio
requst_set = set()
start_times = 0
first = False


class BaseHandler(RequestHandler):
    def get(self):
        print("sss")
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
        # print(f"received request，and request info :{repr(self.request)}")
        return super().prepare()

    def on_finish(self):
        '''
        服务端发送完数据时调用，此处可做一些清理工作
        '''
        # print(f"the response has been sent to the client, request info :{str(self.request)}")



class IndexHandler(RequestHandler):

    def get(self):
        self.write("<a href='"+self.reverse_url("login")+"'>用户登录</a>")


class RegistHandler(RequestHandler):
    def initialize(self, title):
        self.title = title

    def get(self):
        self.write("注册业务处理:" + str(self.title))


@stream_request_body
class LoginHandler(BaseHandler):

    executor = ThreadPoolExecutor(10)

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        # print(f"data_received....{chunk}")
        self.write("注册业务处理:")

    def head(self):
        print(self.request.body)
        print("head......")

    def options(self):
        print("ssss")

    @gen.coroutine
    def post(self):
        print("ssssssssssssssss")
        body = self.request.body

        result = yield self.handle(body)
        # print(f"host :{self.request.connection.stream.socket.getpeername()}")
        self._response(result)

        # print(time.time()-start_times)

    @run_on_executor
    def handle(self,body):

        try:
            # todo:to do something
            # print(body)
            time.sleep(1)
            1/0
        except Exception as e:
            return None
        return 'non-bloacking'

async def get_aiokafka_producer(loop):
    return AIOKafkaProducer(loop=loop, bootstrap_servers='192.168.11.209:9092')


if __name__ == "__main__":
    app = Application(
        [
            (r"/heartbeat", IndexHandler),
            (r"/register", RegistHandler, {"title": "会员注册"}),
            (r"/log", LoginHandler),
        ]
    )
    # tornado.platform.asyncio.AsyncIOMainLoop().instance()
    ioloop = asyncio.get_event_loop()

    http_server = HTTPServer(app)
    http_server.listen(8888)
    ioloop.run_forever()
    #
    # IOLoop.current().start()

    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # sock.setblocking(0)  # 把监听的socket设置成非阻塞
    # 把监听的socket设置成非阻塞print(app)
    # sockets = tornado.netutil.bind_sockets(port=8000, address='', reuse_port=False)
    # # tornado.process.fork_processes(1)
    # server = tornado.httpserver.HTTPServer(app)
    # server.add_sockets(sockets)
    # tornado.ioloop.IOLoop.instance().start()