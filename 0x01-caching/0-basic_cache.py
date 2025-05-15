#!/usr/bin/python3
""" a basic caching module implementation class. """
BaseCaching = __import__('base_caching').BaseCaching


class BaseCache(BaseCaching):
    """
    Basic cache class inherited from BaseCaching.py

    Attributes:
        MAX_ITEMS: number of items in the cache
    """
    def put(self, key, item):
        """
        adds an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Retreive an item from cache by key"""
        return self.cache_data.get(key, None)
