import aiohttp
import asyncio
session = aiohttp.ClientSession()
async def get_status( id):
    print(id)

    r = await session.post('http://127.0.0.1:8000/log', data={id:id})
    print(r.status, r.read(), id)
    r.close()
    session.close()


tasks = []
for i in range(20):
    tasks.append(asyncio.ensure_future(get_status(id=i)))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()