# Caching

## Description
This project covers caching algorithms: what a caching system is, and how
FIFO, LIFO, LRU, MRU, and LFU replacement policies each decide what to evict
when the cache is full.

## Resources
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_in_first_out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_in_first_out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_recently_used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_frequently_used_(LFU))

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- What a caching system is
- What FIFO, LIFO, LRU, MRU, and LFU mean
- The purpose of a caching system
- What limits a caching system has

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3` (the platform-provided `base_caching.py` and `*-main.py` files keep their original `#!/usr/bin/python3` shebang)
- Code follows the `pycodestyle` style (version 2.5)
- All files are executable
- All modules, classes, and functions are documented with real, explanatory docstrings
- Every cache class inherits from `BaseCaching` and uses `self.cache_data`

## Tasks
| File | Description |
| --- | --- |
| `base_caching.py` | Parent class provided by the platform; all caches inherit from it |
| `0-basic_cache.py` | `BasicCache` - no eviction, unlimited size |
| `1-fifo_cache.py` | `FIFOCache` - discards the oldest item put |
| `2-lifo_cache.py` | `LIFOCache` - discards the last item put |
| `3-lru_cache.py` | `LRUCache` - discards the least recently used item |
| `4-mru_cache.py` | `MRUCache` - discards the most recently used item |
