from __future__ import print_function

from twisted1.internet.protocol import DatagramProtocol
from twisted1.internet import reactor


class Echo(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        self.transport.write(data, addr)
        #self.transport.loseConnection()


reactor.listenUDP(9999, Echo())
reactor.run()