#!/usr/bin/env python3
""" Comment function """
from typing import Any, Dict
import csv
import math
from typing import List


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
    stardindex = (page - 1) * page_size
    endindex = stardindex + page_size
    return (stardindex, endindex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Implement a method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10.
        Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset (i.e. the
        correct list of rows).
        If the input arguments are out of range for the dataset, an empty list
        should be returned.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        startindex, endindex = index_range(page, page_size)
        cache_d = self.dataset()
        if startindex >= len(cache_d):
            return []
        return cache_d[startindex:endindex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Implement a get_hyper method that takes the same
        arguments (and defaults) as get_page and returns
        a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        all_size = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < all_size else None
        previous_page = page - 1 if page > 1 else None
        return {"page_size": len(self.get_page(page, page_size)),
                "page": page,
                "data": self.get_page(page, page_size),
                "next_page": next_page,
                "prev_page": previous_page,
                "total_pages": all_size
                }
