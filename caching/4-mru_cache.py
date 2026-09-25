#!/usr/bin/env python3
"""Module for a MRU caching system."""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system that discards the most recently used item."""

    def __init__(self):
        """Initialize the cache and its usage-order tracking list."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item, discarding the most recently used if full."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Return the cached item for key, marking it as recently used."""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
