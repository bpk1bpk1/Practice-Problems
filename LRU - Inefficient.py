class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}
        self.tm = 0

    def get(self, key):
        print("Getting the particular key", key)
        if key in self.cache:
            self.tm += 1
            self.lru[key] = self.tm
            return self.cache[key]
        else:
            return("Value Error")

    def set(self,key,value):
        print("Setting the value", key, value)
        if len(self.cache) >= self.capacity:
            #old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            least_recentkey = min(self.lru.keys(), key = lambda k:self.lru[k])
            self.lru.pop(least_recentkey)
            self.cache.pop(least_recentkey)

        self.tm += 1
        self.cache[key] = value
        self.lru[key] = self.tm

    def print(self):
        for key, value in self.cache.items():
            print(key,":",value)

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
cache.set(4,8)
cache.print()
cache.set(50,100)
cache.print()
