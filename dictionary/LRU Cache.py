# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        else:
            self.cache.move_to_end(key=key,last=True)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key]=value
        self.cache.move_to_end(key=key,last=True)
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)