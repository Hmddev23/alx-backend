#!/usr/bin/python3
"""
define a BasicCache class which inherits from BaseCaching.
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    a caching system that inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        add an item to the cache with the given key.
        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to be stored in the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve an item from the cache by its key.
        Args:
            key (str): The key of the item to be retrieved.
        Returns:
            The item stored in the cache with the specified key,
            or None if the key is not found.
        """
        return self.cache_data.get(key)
