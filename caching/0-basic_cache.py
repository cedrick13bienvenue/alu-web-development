#!/usr/bin/env python3
"""Module for a basic, limitless caching system."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system that stores items with no limit."""

    def put(self, key, item):
        """Add an item to the cache under the given key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the cached item for key, or None if it is absent."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
