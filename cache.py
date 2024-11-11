from cachetools import TTLCache

class Cache:
    def __init__(self, max_size=100, ttl=300):
        # max_size defines the maximum number of items, ttl defines the time to live (in seconds)
        self.cache = TTLCache(maxsize=max_size, ttl=ttl)

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value
