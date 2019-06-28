'''

Args:
Returns:
'''
import threading
import time
e=threading.Event()#事件
def  goevent():
    # e=threading.Event()#事件
    def  go():
        while True:
            # e.wait(3)    #等待,后续代码不再执行，等待set再执行。让线程有序执行
            print("go")
            time.sleep(3)

    threading.Thread(target=go).start()#开启一个线程
    return e
time.sleep(3)
t=goevent()
print(time.time())
time.sleep(2)
print('eeee')
print(time.time())
# while True:
#     e.wait(1)
#     print("main")
