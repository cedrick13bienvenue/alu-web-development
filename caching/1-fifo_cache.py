#!/usr/bin/env python3
"""Module for a FIFO caching system."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that discards the oldest item when full."""

    def put(self, key, item):
        """Add an item, discarding the oldest one if over the limit."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """Return the cached item for key, or None if it is absent."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
