import time
from collections import OrderedDict 

class LRUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            self.cache.move_to_end(key)
            val = self.cache[key]
            
        return val
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.max_capacity:
            self.cache.popitem(last = False)    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# [null,-1,null,-1,null,null,2,6]
l = LRUCache(2)
l.get(2)
l.put(2, 6)
l.get(2)
l.put(1, 5)
l.put(1, 2)
l.get(1)
l.get(2)
