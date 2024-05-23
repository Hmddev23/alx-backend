#!/usr/bin/python3
"""
define a MRUCache class which inherits from BaseCaching.
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        initialize the MRUCache instance by calling
        the parent class initializer.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        adds an item to the cache with the given key.
        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to be stored in the cache.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop()
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        retrieve an item from the cache by its key.
        Args:
            key (str): The key of the item to be retrieved.
        Returns:
            The item stored in the cache with the specified key,
            or None if the key is not found.
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
