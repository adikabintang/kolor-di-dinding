class DoublyLinkedList:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkedList() # head is the most recent
        self.tail = DoublyLinkedList() # tail is the least recent
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __append_on_head(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
    
    def __move_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.__append_on_head(node)
    
    def __pop_tail(self) -> DoublyLinkedList:
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return node
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.__move_to_head(node)
        else:
            node = DoublyLinkedList(key, value)
            if len(self.cache) >= self.capacity:
                least_used_node = self.__pop_tail()
                del self.cache[least_used_node.key]

            self.cache[key] = node
            self.__append_on_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.__move_to_head(node)
        return node.val

l = LRUCache(2)
l.put(1, 1)
l.put(2, 2)
print(l.get(1))
l.put(3, 3)
print(l.get(2))
l.put(4, 4)
print(l.get(1))
print(l.get(3))
print(l.get(4))
