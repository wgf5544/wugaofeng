from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import socket
import tornado
import functools
class IndexHandler(RequestHandler):

    def get(self):
        self.write("<a href='"+self.reverse_url("login")+"'>用户登录</a>")


class RegistHandler(RequestHandler):
    def initialize(self, title):
        self.title = title

    def get(self):
        self.write("注册业务处理:" + str(self.title))


class LoginHandler(RequestHandler):
    def get(self):
        self.write("用户登录页面展示")

    def post(self):

        body = self.request.body
        print(body)
        self.write({'age':12})
        self.flush()
        self.finish()


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
    sockets = tornado.netutil.bind_sockets(port=8000, address='127.0.0.1', reuse_port=True)
    tornado.process.fork_processes(2)
    server = tornado.httpserver.HTTPServer(app)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()