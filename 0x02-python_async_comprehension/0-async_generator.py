#!/usr/bin/env python3
""" Asyncio, Generator and random import modules """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Write a coroutine called async_generator that takes no
    arguments. The coroutine will loop 10 times, each time
    asynchronously wait 1 second, then yield a random
    number between 0 and 10.
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
