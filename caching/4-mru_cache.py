from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class that implements a Most Recently Used (MRU) caching system """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache, following MRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing item to update its position in the MRU order
            self.cache_data.pop(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the most recently used item (the last item in the OrderedDict)
            discarded_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
