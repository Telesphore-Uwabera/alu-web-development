#!/usr/bin/env python3
""" 3-lru_cache module """

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache is a caching system that uses the LRU algorithm.
    It inherits from BaseCaching and adds functionality to discard
    the least recently used item when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """ Initialize the LRU Cache. """
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain order of access

    def put(self, key, item):
        """ Add an item to the cache with LRU algorithm.
        If the number of items exceeds MAX_ITEMS, discard
          the least recently used one.
        """
        if key is None or item is None:
            return

        # If the key already exists, we should move it to 
        # the end to show that it was recently used
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        
        self.cache_data[key] = item

        # If cache exceeds the MAX_ITEMS, pop the first
        #  item which is the least recently used
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item in the OrderedDict
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item from the cache.
        If key is None or not in cache, return None.
        Move the key to the end to show it was recently accessed.
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed key to the end to show it was recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
