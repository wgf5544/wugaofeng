__author__ = 'wgf'
__date__ = ' 下午10:29'
import time

from twisted.internet import reactor, defer

class Getter:
    def gotResults(self, x):
        """
        The Deferred mechanism prgitovides a mechanism to signal error
        conditions.  In this case, odd numbers are bad.

        This function demonstrates a more complex way of starting
        the callback chain by checking for expected results and
        choosing whether to fire the callback or errback chain
        """
        if self.d is None:
            print("Nowhere to put results")
            return

        d = self.d
        self.d = None
        if x % 2 == 0:
            d.callback(x*3)
        else:
            d.errback(ValueError("You used an odd number!"))

    def _toHTML(self,r):
        """
        This function converts r to HTML.

        It is added to the callback chain by getDummyData in
        order to demonstrate how a callback passes its own result
        to the next callback
        """
        print("开始操作")
        time.sleep(10)
        print("操作结束")
        # return "Result: %s" % r

    def getDummyData(self):
        """
        The Deferred mechanism allows for chained callbacks.
        In this example, the output of gotResults is first
        passed through _toHTML on its way to printData.

        Again this function is a dummy, simulating a delayed result
        using callLater, rather than using a real asynchronous
        setup.
        """
        self.d = defer.Deferred()
        # simulate a delayed result by asking the reactor to schedule
        # gotResults in 2 seconds time
        # reactor.callLater(2, self.gotResults, x)

        self.d.addCallback(self._toHTML)
        return self.d

    def start(self):
        deferred = self.getDummyData()
        deferred.callback('ssssssss')




def cbPrintData(result):
    print(result)

def ebPrintError(failure):
    import sys
    sys.stderr.write(str(failure))

# this series of callbacks and errbacks will print an error message
g1 = Getter()
d1=g1.getDummyData()


# this series of callbacks and errbacks will print "Result: 12"
g = Getter()
d=g.getDummyData()
d1.callback('ssssssss1')
d.callback('ssssssss2')

#reactor.callLater(4, reactor.stop)
reactor.run()
