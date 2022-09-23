#!/usr/bin/env python3
""" Father Inheritance """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Create a class BasicCache that
    inherits from BaseCaching and
    is a caching system:
    This caching system doesn’t have limit.
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if (key is None or self.cache_data.get(key) is None):
            return None
        return self.cache_data[key]
