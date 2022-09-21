#!/usr/bin/env python3
""" Asyncio and time module and import previo task file. """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Create a measure_time function with integers
    n and max_delay as arguments that measures
    the total execution time for wait_n, and
    returns total_time / n. Your function
    should return a float.
    """
    firts_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - firts_time
    return total_time / n
