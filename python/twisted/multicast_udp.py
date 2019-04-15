__author__ = 'wgf'
__date__ = ' 下午4:49'

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


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
        print("From client Datagram %s received from %s" % (repr(datagram), repr(address)))
        if datagram:
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write("Server: {}".format(datagram).encode(), address)


# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
# listenMultiple=True 服务端和客户端可以运行在同一个主机上
reactor.listenMulticast(9999, MulticastPingPong(),
                        listenMultiple=True)
reactor.run()