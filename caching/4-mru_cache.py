#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements
    a Most Recently Used (MRU) caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        
        If the cache exceeds its maximum size, discard the most
        recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add/Update the cache
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the order since this key was most recently accessed
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
