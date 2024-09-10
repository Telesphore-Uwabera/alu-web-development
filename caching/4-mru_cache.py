#!/usr/bin/env python3
""" 4-mru_cache module """

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system that uses the MRU algorithm.
    It inherits from BaseCaching and adds functionality to discard
    the most recently used item when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """ Initialize the MRU Cache. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using the MRU algorithm.
        If the number of items exceeds MAX_ITEMS, discard the most recently used one.
        """
        if key is None or item is None:
            return

        # If key already exists, delete it so we can add it back as the most recently used
        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        # If cache exceeds the MAX_ITEMS, pop the last item which is the most recently used
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item from the cache.
        If key is None or not in cache, return None.
        Move the key to the end to show it was recently accessed.
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
