#!/usr/bin/env python3
""" Father Inheritance """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Create a class LIFOCache that
    inherits from BaseCaching and
    is a caching system.
    """
    lk = ""

    def put(self, key, item):
        """
        Discard the last item put
        in cache (LIFO algorithm).
        """
        if (key and item):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                fi = self.lk
                print("DISCARD: {}".format(fi))
                self.cache_data.pop(fi)
            self.lk = key

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if (key is None or self.cache_data.get(key) is None):
            return None
        return self.cache_data[key]
