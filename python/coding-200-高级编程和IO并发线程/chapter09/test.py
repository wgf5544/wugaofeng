__author__ = 'wgf'
__date__ = ' 下午9:34'

def gen_test():
    i=0
    while i<5:
        temp = yield i
        print(temp)
        i+=1

a=gen_test()
a.__next__()
a.__next__()
a.__next__()