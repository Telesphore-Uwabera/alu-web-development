#!/usr/bin/env python3
""" 1-fifo_cache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that uses the FIFO algorithm.
    It inherits from BaseCaching and adds functionality to discard
    the oldest items when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """ Initialize the FIFO Cache. """
        super().__init__()
        self.order = []  # to keep track of the insertion order

    def put(self, key, item):
        """ Add an item to the cache with FIFO algorithm.
        If the number of items exceeds MAX_ITEMS, discard the oldest one.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing key to re-add it as the newest
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)  # Remove the first inserted key
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Get an item from the cache.
        If key is None or not in cache, return None.
        """
        return self.cache_data.get(key, None)
