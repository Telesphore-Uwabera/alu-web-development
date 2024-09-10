#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements
    a Least Frequently Used (LFU) caching system.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.frequency = {}  # Store the frequency of each key
        self.order = {}      # Store the order of access (for LRU within LFU)

    def put(self, key, item):
        """
        Add an item in the cache.

        If the cache exceeds its maximum size, discard the least
        frequently used item. If there's a tie, discard the least
        recently used item among the tied ones.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item in cache
            self.cache_data[key] = item
            # Increment the frequency
            self.frequency[key] += 1
            # Update the order for LRU tie-breaking
            self.order[key] = len(self.cache_data)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.frequency.values())
                least_used = [k for k, v in self.frequency.items() if v == min_freq]

                # If there's a tie, use LRU (least recent in order)
                if len(least_used) > 1:
                    lru_key = min(least_used,
                                   key=lambda k: self.order[k])
                else:
                    lru_key = least_used[0]

                # Discard the LFU (and possibly LRU) item
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.order[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new item
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order[key] = len(self.cache_data)

    def get(self, key):
        """
        Get an item by key.

        Update the frequency of the key since it's being accessed.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and order
        self.frequency[key] += 1
        self.order[key] = len(self.cache_data)

        return self.cache_data[key]
