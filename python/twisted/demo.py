__author__ = 'wgf'
__date__ = ' 下午2:47'

import time
import requests

from twisted.internet import reactor,task,defer
from twisted.web.client import Agent
from twisted.web.http_headers import Headers


def hello(name):
    print("Hello world!===>", name, '===>',str(int(time.time())))


# 同步请求，阻塞程序
def request_google():
    res = requests.get('http://www.google.com')
    return res


# 异步请求（twisted自带的httpclient是异步的，不会阻塞reactor的运行）
@defer.inlineCallbacks
def request_google_asyn():
    agent = Agent(reactor)
    try:
        result = yield agent.request('GET', 'http://www.google.com'.encode(), Headers({'User-Agent': ['Twisted Web Client Example']}), None)
    except Exception as e:
        print(e)
        return
    print(result)

# task任务每10秒运行一次
# task1 = task.LoopingCall(hello, 'ding-tasklooping')
# task1.start(2)

'''
　 异步非阻塞模式：
        一定要返回twisted的defer的对象（延迟对象），要求第三方库API支持异步版本；
        现实中不可能每个API都支持异步版本。
   线程模式：
        如果函数功能不是特别复杂，都可以使用twsited提供的线程模式。
        建议不要大量使用线程模式，效率低下，大量浪费CPU资源。只要有异步库，优先使用异步库。
        线程模式只是做非常简单而不频繁的操作。
'''

reactor.callWhenRunning(hello, 'ding-callwhen')
# reactor.callLater(1, request_google) # 普通请求会阻塞程序
#reactor.callLater(1, request_google_asyn)  # twisted异步请求，非阻塞，
reactor.callInThread(request_google)  # 线程模式，

reactor.callLater(3, hello, 'yuyue')

reactor.run()