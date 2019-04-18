__author__ = 'wgf'
__date__ = ' 下午6:49'

import time

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import defer,utils

'''
#长连接数量太多，导致服务器异常，此时已经无法挽救，只能重启服务。
#如何解决长连接问题：

from twisted.protocols.policies import TimeoutMixin

class TimeoutTester(protocol.Protocol, policies.TimeoutMixin):
    conn_timeout = 3
    data_timeout = 300
    def connectionMade(self):
        self.setTimeout(self.conn_timeout)
    def dataReceived(self, data):
        self.setTimeout(self.data_timeout)
    def connectionLost(self, reason=None):
        self.setTimeout(None)
'''


class TcpEchoServer(Protocol):

    def dataReceived(self, data): #将收到的数据返回给客户端
        print('From TCP client data:{}'.format(data))
        reactor.callInThread(self.handle, data)

        #self.transport.loseConnection()

    def handle(self,data):
        print('开始操作')
        time.sleep(5)
        reactor.callFromThread(self.write_response, data)
        print('结束操作')

    def write_response(self, result):
        self.transport.write("ack:".encode() + result )

class MulticastPingPong(DatagramProtocol):

    def startProtocol(self):
        """
        Called after protocol has started listening.
        """
        # Set the TTL>1 so multicast will cross router hops:
        # 设置数据包存活时间（即路由转发数），TTL>1意味着跨路由转发。最大值255
        self.transport.setTTL(5)
        # Join a specific multicast group:
        # 设置加入组播组地址
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagram, address):
        print("From UDP client data:%s received from %s" % (repr(datagram), repr(address)))
        if datagram:

            time.sleep(10)
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write(datagram, address)


# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
# listenMultiple=True 服务端和客户端可以运行在同一个主机上
# 将udp多播加入到reactor事件循环中
reactor.listenMulticast(9999, MulticastPingPong(),
                        listenMultiple=True)

# 将tcp连接加入到事件驱动中
factory = Factory()
factory.numProtocols = 0
factory.protocol = TcpEchoServer
port = 1200
reactor.listenTCP(9999, factory)


reactor.run()