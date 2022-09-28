from ast import arguments
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
        assert type(page) == int and page > 0 and type(
            page_size) == int and page_size > 0
        startindex, endindex = index_range(page, page_size)
        cache_d = self.dataset()
        if startindex >= len(cache_d):
            return []
        return cache_d[startindex:endindex]
