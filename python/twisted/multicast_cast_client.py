__author__ = 'wgf'
__date__ = ' 下午5:31'

import multiprocessing

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor,task


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:9999 - all listeners on the multicast address
        # (including us) will receive this message.
        i = repr(multiprocessing.Process.name)
        def sendto(s):

            self.transport.write(s.encode(), ("228.0.0.5", 9999))  # 设置组内能接收信息的目的端口
        task1 = task.LoopingCall(sendto, i)
        task1.start(1)

    def datagramReceived(self, datagram, address):
        print("From UDP server data: %s received from %s" % (repr(datagram), repr(address)))


# task1.start(2)

# 组播组客户端也需要设置监听端口
reactor.listenMulticast(10001, MulticastPingClient(), listenMultiple=True)
reactor.run()