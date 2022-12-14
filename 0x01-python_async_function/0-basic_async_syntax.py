#!/usr/bin/env python3
""" Asyncio and random modules. """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Write an asynchronous coroutine that
    takes in an integer argument named wait_random
    that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    sleeping = random.uniform(0, max_delay)
    await asyncio.sleep(sleeping)
    return sleeping
