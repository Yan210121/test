#coding:utf-8
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
    # 一旦有数据到来就返回一个回应
        print(data)
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        print("EchoFactory buildProtocol")
        return Echo()

reactor.listenTCP(8000, EchoFactory())
reactor.run()