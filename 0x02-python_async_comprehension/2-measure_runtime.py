#!/usr/bin/env python3
""" Asyncio, time and previous file import. """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    write a measure_runtime coroutine
    that will execute async_comprehension
    four times in parallel using (asyncio.gather).
    measure_runtime should measure the total runtime
    and return it. Notice that the total runtime is
    roughly 10 seconds.
    """
    firts_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total_time = time.time() - firts_time
    return total_time
