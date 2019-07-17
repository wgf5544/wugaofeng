import asyncio
import concurrent
import time
from typing import Optional
from multiprocessing import Queue, Process

pool = concurrent.futures.ThreadPoolExecutor()

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        # print(data)
        # self.transport.set_write_buffer_limits(low=0)
        print(f"buffer size:{self.transport.get_write_buffer_size()}")
        message = data.decode()
        print('Data received: {!r}'.format(message))
        # asyncio.run(self.main(pool))
        # print('Send: {!r}'.format(message))
        self.transport.write(data)
        print(f"buffer size:{self.transport.get_write_buffer_size()}")

        # print('Close the client socket')
        self.transport.close()

    def eof_received(self) -> Optional[bool]:
        return super().eof_received()

    def connection_lost(self, exc: Optional[Exception]) -> None:
        super().connection_lost(exc)
        print("connection closed.....")

    def pause_writing(self) -> None:
        print("pause...")
        super().pause_writing()

    def resume_writing(self) -> None:
        print("resume...")
        super().resume_writing()

    async def slow_operation(self,future):
        await asyncio.sleep(1)
        future.set_result('Future is done!')

    def got_result(self,future):
        print(future.result())
        loop.stop()

    def handler(self):
        time.sleep(1)
        print(time.time())
        return "111222333"

    async def main(self,pool):
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            pool, self.handler)
        print(result)

import os

def run():
    time.sleep(2)
    print(f"proccess:{os.getpid()}")

if __name__ == "__mian__":


    p = Process(target=run)
    p.start()

    print("process started....")
    loop = asyncio.get_event_loop()



    # Each client connection will create a new protocol instance
    coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
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