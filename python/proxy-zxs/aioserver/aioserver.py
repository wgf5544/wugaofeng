import uuid
import logging
import asyncio
import aiohttp
import socket
from functools import partial
from aiohttp import web
from collections import namedtuple
from itertools import islice

logger = logging.getLogger(__name__)

Connection = namedtuple('Connection', ('transport', 'channel'))

def limited_as_completed(coros, limit):
    """
    collect future
    :param coros:
    :param limit:
    :return:
    """
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

class Channel(object):

    """Duplex communication channel, can be seen as a basic pipe, constituted by two asynchronous
    queue"""

    def __init__(self):
        self.req = asyncio.Queue()
        self.res = asyncio.Queue()

    async def push_request(self, request):
        return await self.req.put(request)

    async def push_response(self, response):
        return await self.res.put(response)

    async def pull_request(self):
        data = await self.req.get()
        self.req.task_done()
        return data

    async def pull_response(self):
        data = await self.res.get()
        self.res.task_done()
        return data

class BaseTunnelProtocol(asyncio.Protocol):

    def __init__(self, loop):
        self.loop = loop
        self.transport = None
        self._shutdown = asyncio.Event()
        self.logger = logging.getLogger('aiotunnel.protocol.BaseTunnelProtocol')

    def connection_made(self, transport):
        self.transport = transport
        self.transport.set_write_buffer_limits(0)
        sock = transport.get_extra_info('socket')
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    def connection_lost(self, exc):
        self.logger.debug('The server closed the connection')
        self.transport.close()

    def eof_received(self):
        self.logger.debug('No more data to receive')
        self.transport.close()

    def close(self):
        self._shutdown.set()


class TunnelProtocol(BaseTunnelProtocol):

    def __init__(self, loop, channel):
        self.channel = channel
        self.logger = logging.getLogger('aiotunnel.protocol.TunnelProtocol')
        super().__init__(loop)

    def connection_made(self, transport):
        super().connection_made(transport)
        self.loop.create_task(self.async_consume_request())


    def data_received(self, data):
        self.loop.create_task(self.channel.push_response(data))


    async def async_consume_request(self):
        while not self._shutdown.is_set():
            try:
                request = await self.channel.pull_request()
            except asyncio.CancelledError:
                self.logger.debug("Cancelled pull task")
            else:
                await self.loop.run_in_executor(None, self.transport.write, request)


class Handler(object):

    def __init__(self, app, reverse=False):
        self.reverse = reverse
        self.conn = None
        self.tunnels = {}
        self.app = app
        self.app.add_routes([
            web.post('/aiotunnel', self.post_aiotunnel),
            web.put('/aiotunnel/{cid}', self.put_aiotunnel),
            web.get('/aiotunnel/{cid}', self.get_aiotunnel),
            web.delete('/aiotunnel/{cid}', self.delete_aiotunnel)
        ])
        self.logger = logging.getLogger('aiotunnel.tunneld.Handler')


    def close_all_tunnels(self):
        if self.conn:
            self.conn.close()
        for _, conn in self.tunnels.items():
            if conn.transport is not None:
                conn.transport.close()
        pending = asyncio.all_tasks()
        for task in pending:
            if not task.cancelled():
                task.cancel()

    async def push_request(self, cid, request):
        if cid not in self.tunnels:
            return
        return await self.tunnels[cid].channel.push_request(request)

    async def pull_response(self, cid):
        return await self.tunnels[cid].channel.pull_response()

    async def open_connection(self, host, port, channel):

        # loop = asyncio.get_running_loop()

        loop = asyncio.get_event_loop()
        transport, protocol = await loop.create_connection(
            lambda: TunnelProtocol(loop, channel),
            host, port
        )
        self.conn = protocol
        return transport

    async def create_endpoint(self, host, port, channel):
        # Get a reference to the event loop as we plan to use
        # low-level APIs.
        # loop = asyncio.get_running_loop()
        loop = asyncio.get_event_loop()
        server = await loop.create_server(
            lambda: TunnelProtocol(loop, channel), host, port, reuse_port=True
        )
        self.conn = server
        async with server:
            await server.serve_forever()

    async def post_aiotunnel(self, request):

        cid = uuid.uuid4()
        service = await request.text()
        channel = Channel()
        host, port = service.split(':')
        if self.reverse:
            self.logger.info("Opening local port %s", port)
            loop = asyncio.get_running_loop()
            loop.create_task(self.create_endpoint(host, int(port), channel))
            self.tunnels[str(cid)] = Connection(None, channel)
        else:
            self.logger.info("Opening connection with %s:%s", host, port)
            transport = await self.open_connection(host, int(port), channel)
            self.tunnels[str(cid)] = Connection(transport, channel)

        print(len(self.tunnels), cid)
        return web.Response(text=str(cid))

    async def put_aiotunnel(self, request):
        cid = request.match_info['cid']
        if cid not in self.tunnels:
            return web.Response()
        data = await request.read()
        # print("put", data)
        await self.push_request(cid, data)
        return web.Response()

    async def get_aiotunnel(self, request):
        cid = request.match_info['cid']
        if cid not in self.tunnels:
            return web.Response()
        result = await self.pull_response(cid)
        # print("get", result)
        return web.Response(body=result)

    async def delete_aiotunnel(self, request):
        cid = request.match_info['cid']
        if cid not in self.tunnels:
            return web.Response()
        self.tunnels[cid].transport.close()
        del self.tunnels[cid]
        return web.Response()

async def on_shutdown_coro(app, handler):
    handler.close_all_tunnels()
    await app.shutdown()


def start_tunneld(host, port, reverse=False, cafile=None, certfile=None, keyfile=None):
    app = web.Application()
    handler = Handler(app, reverse)
    on_shutdown = partial(on_shutdown_coro, handler=handler)
    app.on_shutdown.append(on_shutdown)
    try:
        web.run_app(app, host=host, port=port, access_log=logger,
                    access_log_format='"%r" %s %b %Tf %a - "%{User-agent}i"')
    except:
        logger.info("Shutdown")

if __name__ == '__main__':

    start_tunneld(host="0.0.0.0", port=8080)