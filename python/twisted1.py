__author__ = 'wgf'
__date__ = ' 上午12:00'


from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory


class EchoServer(Protocol):

    def dataReceived (self, data): #将收到的数据返回给客户端
        self.transport.write(data)
        self.transport.loseConnection()
        print (data)



factory = Factory()
factory.numProtocols = 0
factory.protocol = EchoServer

port = 1200
reactor.listenTCP(port, factory)
reactor.run()

