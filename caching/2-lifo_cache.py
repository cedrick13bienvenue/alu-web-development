#!/usr/bin/env python3
"""Module for a LIFO caching system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system that discards the last item put when full."""

    def __init__(self):
        """Initialize the cache and its put-order tracking list."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item, discarding the last one put if over the limit."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order[-1]
            del self.cache_data[last_key]
            self.order.remove(last_key)
            print("DISCARD: {}".format(last_key))
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Return the cached item for key, or None if it is absent."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
