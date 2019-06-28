'''

Args:
Returns:
'''

import asyncio
from aiokafka import AIOKafkaProducer
import traceback


loop = asyncio.get_event_loop()

async def send_one():
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers="192.168.11.209")

    await producer.start()
    try:

        await producer.send_and_wait("my_topic", b"Super message")
    finally:
        await producer.stop()

loop.run_until_complete(send_one())