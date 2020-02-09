class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_ll(head: Node):
    current = head
    while current:
        print(current.val)
        current = current.next

def remove_middle(n: Node):
    n.val = n.next.val
    n.next = n.next.next
    n.next = None

head = Node(9)
a = Node(9)
b = Node(7)
c = Node(9)

head.next = a
a.next = b
b.next = c

print_ll(head)
print("---")
remove_middle(b)
print_ll(head)
