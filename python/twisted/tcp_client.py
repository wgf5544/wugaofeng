__author__ = 'wgf'
__date__ = ' 下午7:06'
from twisted.internet.protocol import DatagramProtocol
import time

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout

class Echo(Protocol):

    def connectionMade(self):
        self.transport.write('hello TCP server,I am TCP client!!!!! '
                             'hello TCP server,I am TCP client!!!!! '
                             'hello TCP server,I am TCP client!!!!!'
                             'hello TCP server,I am TCP client!!!!!'
                             'hello TCP server,I am TCP client!!!!!'.encode())

    def dataReceived(self, data):

        #stdout.write(data)
        print('From TCP server data:{}'.format(data))
        self.transport.write(data)
    def connectionLost(self, reason):
        print('TCP client close reason:{}'.format(reason))

class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected.')
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)


reactor.connectTCP('localhost', 8888, EchoClientFactory())
reactor.run()