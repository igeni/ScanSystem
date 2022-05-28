class Cache:
    """
    cache for avoid extra work
    """
    cache = {}

    def init_cache(self, values:list):
        for item in values:
            self.add(item)

    def add(self, val:str):
        self.cache[val] = True

    def remove(self, val:str):
        self.cache.pop(val, None)

    def check(self, val:str):
        return bool(self.cache.get(val, False))

