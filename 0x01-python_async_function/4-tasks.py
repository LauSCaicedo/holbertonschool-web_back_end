#!/usr/bin/env python3
""" Asyncio module and import previo file. """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alter it into a new
    function task_wait_n. The code is nearly identical
    to wait_n except task_wait_random is being called.
    """
    list_a: List[float] = []
    temp1: List[float] = []
    for x in range(n):
        list_a.append(task_wait_random(max_delay))
    for z in asyncio.as_completed(list_a):
        result = await z
        temp1.append(result)
    return temp1
