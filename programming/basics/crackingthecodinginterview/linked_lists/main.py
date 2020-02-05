class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def remove_duplicate(self):
        current = self.head
        counter = 0
        while current:
            iterator = head
            before = iterator
            while iterator:
                if iterator.val == current.val:
                    counter += 1
                
                if counter == 2:
                    before.next_node = iterator.next_node
                    iterator = None
                    break

                before = iterator
                iterator = iterator.next_node
            
            counter = 0
            current = current.next_node

    def print_all(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next_node

head = Node(9)
a = Node(9)
b = Node(7)

head.next_node = a
a.next_node = b

l = LinkedList(head)
l.print_all()
l.remove_duplicate()
print("---")
l.print_all()