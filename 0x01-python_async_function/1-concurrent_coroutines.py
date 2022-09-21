#!/usr/bin/env python3
""" Asyncio module and import previo file. """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> list:
    """
    write an async routine called wait_n that
    takes in 2 int arguments n and max_delay.
    You will spawn wait_random n times with
    the specified max_delay. wait_n should
    return the list of all the delays. The list of
    the delays should be in ascending order
    without using sort()
    """
    list_a: list = []
    temp1: list = []
    temp2: list = []
    for x in range(n):
        list_a.append(wait_random(max_delay))
    for z in asyncio.as_completed(list_a):
        result = await z
        temp1.append(result)
    temp2 = list_a
    list_a = temp1
    return list_a
