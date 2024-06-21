# O(1) get and put

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ord = []
        self.pairs = dict()


    # O(N) solutioon
    def get(self, key: int) -> int:
        if key not in self.pairs.keys(): return -1

        self.ord.pop(self.ord.index(key))
        self.ord.append(key)
        return self.pairs[key]

    # O(1) probably?
    def put(self, key: int, value: int) -> None:
        # find key val pair, re-add to back with new value
        if key in self.pairs.keys():
            self.pairs[key] = value
            self.ord.pop(self.ord.index(key))
            self.ord.append(key)
            return

        # must be new key, may need to evict
        if len(self.pairs) == self.capacity:
            del self.pairs[self.ord[0]]
            self.ord.pop(0)            

        self.pairs[key] = value
        self.ord.append(key)




lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.get(1)    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)    # return -1 (not found)
lRUCache.get(3)    # return 3
lRUCache.get(4)    # return 4