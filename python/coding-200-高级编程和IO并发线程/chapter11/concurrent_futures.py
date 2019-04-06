from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
from multiprocessing import Pool

#未来对象，task的返回容器


#线程池， 为什么要线程池
#主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
#当一个线程完成的时候我们主线程能立即知道
#futures可以让多线程和多进程编码接口一致
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times



executor = ThreadPoolExecutor(max_workers=2)
#通过submit函数提交执行的函数到线程池中, submit 是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))


#要获取已经成功的task的返回
urls = [3,2,4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page".format(data))
#通过executor的map获取已经完成的task的值
# for data in executor.map(get_html, urls):
#     print("get {} page".format(data))


# #done方法用于判定某个任务是否完成
# print(task1.done())
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
#
# #result方法可以获取task的执行结果
# print(task1.result())

#from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutorfrom multiprocessing import Poolimport requestsimport jsonimport osdef get_page(url):    print('<进程%s> get %s' %(os.getpid(),url))    respone=requests.get(url)    if respone.status_code == 200:        return {'url':url,'text':respone.text}def parse_page(res):    res=res.result()    print('<进程%s> parse %s' %(os.getpid(),res['url']))    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))    with open('db.txt','a') as f:        f.write(parse_res)if __name__ == '__main__':    urls=[        'https://www.baidu.com',        'https://www.python.org',        'https://www.openstack.org',        'https://help.github.com/',        'http://www.sina.com.cn/'    ]    # p=Pool(3)    # for url in urls:    #     p.apply_async(get_page,args=(url,),callback=pasrse_page)    # p.close()    # p.join()    p=ProcessPoolExecutor(3)    for url in urls:        p.submit(get_page,url).add_done_callback(parse_page) #parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果

