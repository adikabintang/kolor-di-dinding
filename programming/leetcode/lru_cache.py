import time

# very bad
# Runtime: 6908 ms, faster than 5.01% of Python3 online submissions 
# Memory Usage: 22.8 MB, less than 6.06% of Python3 online submissions 
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.max_capacity = capacity
        self.queue_key_usage = []

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            self.remove_from_q(key)
            val = self.cache[key]
            self.queue_key_usage.append(key)
            
        return val
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_from_q(key)
        
        self.queue_key_usage.append(key)
        if key not in self.cache and len(self.cache) >= self.max_capacity:
            lru_key = self.queue_key_usage.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = value
    
    def remove_from_q(self, item):
        i = 0
        while item != self.queue_key_usage[i]:
            i += 1
        
        val = self.queue_key_usage[i]
        i += 1
        while i < len(self.queue_key_usage):
            self.queue_key_usage[i - 1] = self.queue_key_usage[i]
            i += 1
        
        del self.queue_key_usage[-1]
        


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
