from linkedlist import *

class LRUCache:

    def __init__(self, capacity: int):
        self.time = 0
        self.order = [0 for i in range(capacity)]
        self.map = dict()

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.map[key] = value


sol = LRUCache()

