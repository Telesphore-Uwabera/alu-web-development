#!/usr/bin/env python3
""" 2-lifo_cache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that uses the LIFO algorithm.
    It inherits from BaseCaching and adds functionality to discard
    the most recently added item when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """ Initialize the LIFO Cache. """
        super().__init__()
        self.last_key = None  # To keep track of the most recently added key

    def put(self, key, item):
        """ Add an item to the cache with LIFO algorithm.
        If the number of items exceeds MAX_ITEMS, discard the most recent one.
        """
        if key is None or item is None:
            return

        # Add the item to the cache
        self.cache_data[key] = item

        # If cache exceeds the MAX_ITEMS, discard the last added item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        # Update the last_key to the current one
        self.last_key = key

    def get(self, key):
        """ Get an item from the cache.
        If key is None or not in cache, return None.
        """
        return self.cache_data.get(key, None)

