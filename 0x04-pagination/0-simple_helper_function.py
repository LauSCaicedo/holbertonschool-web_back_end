#!/usr/bin/env python3
def index_range(page, page_size):
    """
    Write a function named index_range
    that takes two integer arguments page
    and page_size. The function should return
    a tuple of size two containing a start
    index and an end index corresponding to
    the range of indexes to return in a list
    for those particular pagination parameters.
    """
    if page == 1:
        stardindex = 0
    else:
        stardindex = (page - 1) * page_size
    endindex = page * page_size
    return (stardindex, endindex)
