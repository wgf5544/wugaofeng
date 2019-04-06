__author__ = 'wgf'
__date__ = ' 下午5:15'

#
# def how_many_ways(n):
#     step = (1, 2, 3)
#
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return 1 +(2 * 3 * how_many_ways(n - 3))
#
#
#
# #print(how_many_ways(6))

import os
import time

print('开始')
pid = os.fork()


if pid == 0:
    print('子进程{}'.format(os.getpid()))
else:
    print('父进程{}'.format(os.getppid()))

time.sleep(2)