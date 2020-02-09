class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def remove_duplicate_n2(self):
        current = self.head
        while current:
            iterator = head
            before = iterator
            counter = 0
            while iterator:
                if iterator.val == current.val:
                    counter += 1
                
                if counter == 2:
                    before.next_node = iterator.next_node
                    iterator = None
                    break

                before = iterator
                iterator = iterator.next_node
            
            current = current.next_node
    
    def remove_duplicate_n(self):
        current = self.head
        counter = {}
        while current:
            if current.val in counter:
                counter[current.val] += 1
            else:
                counter[current.val] = 1
                
            current = current.next_node
        
        current = self.head.next_node
        before = self.head
        while current:
            if counter[current.val] > 1:
                before.next_node = current.next_node
                counter[current.val] -= 1
                current = None
                current = before.next_node
            else:
                before = current
                current = current.next_node

    def print_all(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next_node

head = Node(9)
a = Node(9)
b = Node(7)
c = Node(9)

head.next_node = a
a.next_node = b
b.next_node = c

l = LinkedList(head)
l.print_all()
# l.remove_duplicate_n2()
l.remove_duplicate_n()
print("---")
l.print_all()