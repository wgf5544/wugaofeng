import asyncio
import logging
import socket
import iofree
import aiohttp

logger = logging.getLogger(__name__)
PACKET_SIZE = 1024 * 8

proxy_url = "http://127.0.0.1:8080/aiotunnel"


def pack_addr(addr) -> bytes:
    host, port = addr
    try:  # IPV4
        packed = b"\x01" + socket.inet_aton(host)
    except OSError:
        try:  # IPV6
            packed = b"\x04" + socket.inet_pton(socket.AF_INET6, host)
        except OSError:  # hostname
            packed = host.encode("ascii")
            packed = b"\x03" + len(packed).to_bytes(1, "big") + packed
    return packed + port.to_bytes(2, "big")


def read_addr():
    atyp = yield from iofree.read(1)
    if atyp == b"\x01":  # IPV4
        data = yield from iofree.read(4)
        host = socket.inet_ntoa(data)
    elif atyp == b"\x04":  # IPV6
        data = yield from iofree.read(16)
        host = socket.inet_ntop(socket.AF_INET6, data)
    elif atyp == b"\x03":  # hostname
        data = yield from iofree.read(1)
        data += yield from iofree.read(data[0])
        host = data[1:].decode("ascii")
    else:
        raise Exception(f"unknown atyp: {atyp}")
    port, = yield from iofree.read_struct("!H")
    return (host, port)


@iofree.parser
def socks5_request(auth=False):
    parser = yield from iofree.get_parser()
    ver, nmethods = yield from iofree.read_struct("!BB")
    assert ver == 5, f"bad socks version: {ver}"
    assert nmethods != 0, f"nmethods can't be 0"
    methods = yield from iofree.read(nmethods)
    if auth and b"\x02" not in methods:
        parser.write(b"\x05\x02")
        raise Exception("server needs authentication")
    elif b"\x00" not in methods:
        parser.write(b"\x05\x00")
        raise Exception("method not support")
    if auth:
        parser.write(b"\x05\x02")
        auth_ver, username_length = yield from iofree.read_struct("!BB")
        assert auth_ver == 1, f"invalid auth version {auth_ver}"
        username = yield from iofree.read(username_length)
        password_length = (yield from iofree.read(1))[0]
        password = yield from iofree.read(password_length)
        if (username, password) != auth:
            parser.write(b"\x01\x01")
            raise Exception("authenticate failed")
        else:
            parser.write(b"\x01\x00")
    else:
        parser.write(b"\x05\x00")
    ver, cmd, rsv = yield from iofree.read_struct("!BBB")
    if cmd == 1:  # connect
        pass
    elif cmd == 2:  # bind
        raise Exception("doesn't support bind yet")
    elif cmd == 3:  # associate
        raise Exception("doesn't support associate yes")
    else:
        raise Exception(f"unknown cmd: {cmd}")
    target_addr = yield from read_addr()
    return target_addr, cmd


@iofree.parser
def socks5_response(auth):
    data = yield from iofree.read(2)
    assert data[0] == 5, f"bad socks version: {data[0]}"
    method = data[1]
    assert method in (0, 2), f"bad method {data[1]}"
    if auth:
        auth_ver, status = yield from iofree.read_struct("!BB")
        assert auth_ver == 1, f"invalid auth version {auth_ver}"
        assert status == 0, f"invalid status {status}"
    data = yield from iofree.read(3)
    assert data[0] == 5, f"bad socks version: {data[0]}"
    assert data[1] == 0, f"failed REP with code: {data[1]}"
    bind_addr = yield from read_addr()
    return bind_addr

async def pipe(reader, writer):
    """
    pipe stream
    :param reader:
    :param writer:
    :return:
    """
    try:
        while not reader.at_eof():
            data = await reader.read(PACKET_SIZE)
            # print("cccc", data)
            writer.write(data)
            await writer.drain()
    finally:
        writer.close()



async def async_close_remote_connection(cid):
    try:
        async with aiohttp.ClientSession() as session:
            await session.delete(f'{proxy_url}/{cid}', ssl_context=None)
    except (aiohttp.ClientError, asyncio.TimeoutError):
        logger.error(f"Cannot communicate with {proxy_url}/{cid}")
        await asyncio.sleep(5)
    except:
        logger.error("Connection with server lost")
        await asyncio.sleep(5)


async def async_write_data(reader, writer, cid):
    try:
        while not reader.at_eof():
            data = await reader.read(PACKET_SIZE)
            # print("put", data)
            async with aiohttp.ClientSession() as session:
                await session.put(f'{proxy_url}/{cid}', data=data, ssl_context=None)
    finally:
        writer.close()
        print(f"close session:{cid}")
        await async_close_remote_connection(cid)


async def async_read_data(writer, cid):

    try:
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(f'{proxy_url}/{cid}', ssl_context=None) as resp:
                    data = await resp.read()
                    # print("get", data)
                    if data:
                        writer.write(data)
    except asyncio.TimeoutError:
        print(f'timeout: {proxy_url}/{cid}')
        writer.close()


def _make_resp(code=0, host="0.0.0.0", port=0):
    return b"\x05" + code.to_bytes(1, "big") + b"\x00" + pack_addr((host, port))

async def handle_echo(local_reader, local_writer):
    try:

        socks5_parser = socks5_request.parser(False)

        while not socks5_parser.has_result:
            data = await local_reader.read(PACKET_SIZE)
            if not data:
                return
            socks5_parser.send(data)
            data = socks5_parser.read()
            if data:
                local_writer.write(data)
                await local_writer.drain()
        target_addr, cmd = socks5_parser.get_result()
        assert cmd == 1, f"only support connect command {cmd}"

        _addr, _port = target_addr
        print(f"connect {_addr}:{_port}")

        cid = None
        data = f"{_addr}:{_port}".encode()
        async with aiohttp.ClientSession() as session:
            async with session.post(proxy_url, data=data, ssl_context=None) as resp:
                cid = await resp.text()
        # remote_reader, remote_writer = await asyncio.open_connection(
        #     _addr, _port)

        local_writer.write(_make_resp())
        await local_writer.drain()

        # local transport.
        # pipe1 = pipe(local_reader, remote_writer)
        # pipe2 = pipe(remote_reader, local_writer)
        # await asyncio.gather(pipe1, pipe2)

        # print("===========", cid)
        # loop = asyncio.get_event_loop()
        # loop.create_task(async_write_data(local_reader, cid))
        # loop.create_task(async_read_data(local_writer, cid))


        pipe1 = async_write_data(local_reader, local_writer, cid)
        pipe2 = async_read_data(local_writer, cid)
        await asyncio.gather(pipe1, pipe2)

    except Exception as e:
        logger.error(e, exc_info=True)
    # finally:
    #     local_writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 9011, loop=loop)
server = loop.run_until_complete(coro)


# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()