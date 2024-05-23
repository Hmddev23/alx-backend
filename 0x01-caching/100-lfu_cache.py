#!/usr/bin/python3
"""
define an LFUCache class which inherits from BaseCaching.
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initializes the LFUCache instance by calling the parent
        class initializer and setting up a dictionary to keep
        track of the frequency of access for each key.
        """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """
        adds an item to the cache with the given key.
        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                lfu_key = min(least_freq_keys, key=self.freq.get)
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """
        retrieves an item from the cache by its key and
        increments its access frequency.
        Args:
            key (str): The key of the item to be retrieved.
        Returns:
            The item stored in the cache with the specified key,
            or None if the key is not found.
        """
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
