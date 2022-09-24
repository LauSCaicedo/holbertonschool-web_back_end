#!/usr/bin/env python3
""" Father Inheritance """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Create a class FIFOCache that
    inherits from BaseCaching and
    is a caching system.
    """

    def put(self, key, item):
        """
        Discard the first item put
        in cache (FIFO algorithm).
        """
        if (key and item):
            if (key in self.cache_data):
                self.cache_data[key] = item
            else:
                if (len(self.cache_data) > BaseCaching.MAX_ITEMS - 1):
                    fi = list(self.cache_data)[0]
                    print("DISCARD: {}".format(fi))
                    self.cache_data.pop(fi)
                self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if (key is None or self.cache_data.get(key) is None):
            return None
        return self.cache_data[key]
