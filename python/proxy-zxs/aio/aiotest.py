import asyncio
from itertools import islice

def limited_as_completed(coros, limit):
    futures = [
        asyncio.ensure_future(c)
        for c in islice(coros, 0, limit)
    ]
    async def first_to_finish():
        while True:
            await asyncio.sleep(0)
            for f in futures:
                if f.done():
                    futures.remove(f)
                    try:
                        newf = next(coros)
                        futures.append(
                            asyncio.ensure_future(newf))
                    except StopIteration as e:
                        pass
                    return f.result()
    while len(futures) > 0:
        yield first_to_finish()

async def print_when_done(tasks):
    for res in limited_as_completed(tasks, 10):
        print("Result %s" % await res)

async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1.0 / number)
    print("Finishing %d" % number)
    return str(number)

async def print_when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print("Result %s" % await res)

coros = [mycoro(i) for i in range(1, 101)]

loop = asyncio.get_event_loop()
loop.run_until_complete(print_when_done(coros))
loop.close()