import asyncio
import datetime

# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
#
# asyncio.run(display_date())
#
# loop = asyncio.get_running_loop()
# coro = asyncio.sleep(1, result=3)
#
# # Submit the coroutine to a given loop
# future = asyncio.run_coroutine_threadsafe(coro, loop)
#
# # Wait for the result with an optional timeout argument
# assert future.result() == 3
d = {}
d["key"]=4
print(d)

import datetime
import time
# print(time.time())
# i = int("1562659956000")
# print(i)
# date = datetime.datetime.fromtimestamp(1562687999999/1000)
# # 1562659956000
# print(date)
# print(bool("false"))
# print(time.time()*1000)
#
#
# date = datetime.datetime(2019, 2, 26, 15, 27, 28)
# print(date.timestamp())
# print(datetime.datetime.fromtimestamp(date.timestamp()))


s="""
this is #1# 
string example....wow!!! 
this is #2# really #3# 
string
"""
ss=s.replace("#1#","2222").replace("#2#","3333").replace("#3#","4444")
print(ss)
print(s)

print(datetime.datetime.fromtimestamp(1561019323.000))
ss= "s,g"
t = tuple(ss.split())
print("ssA244￥".lower())


def ssss():
    try:
        print("sss")
        return
    except Exception as e:
        print("ffff")
    finally:
        print("gggg")



print(bool(tuple()) is  False)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
import json
print(json.loads(''))