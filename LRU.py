import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        print("Getting the particular key",key)
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        print("Setting the value",key,value)
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
        self.cache[key] = value

    def print(self):
        for key,value in self.cache.items():
            print (key,self.cache[key])

cache = LRUCache(5)
cache.set(10,20)
cache.set(18,36)
cache.set(20,40)
cache.set(30,60)
cache.set(2,4)
cache.get(10)
cache.get(20)
cache.get(18)
cache.get(30)
cache.print()
cache.set(4,8)
cache.print()