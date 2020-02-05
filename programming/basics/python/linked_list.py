class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        i = 0
        while current:
            i += 1
            current = current.get_next_node()
        return i

n = Node(2)
l = LinkedList(n)
l.insert(4)
l.insert(8)

print(l.size())