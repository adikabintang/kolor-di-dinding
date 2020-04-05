class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def is_palindrome(self):
        s = []
        p = self.head
        while p:
            s.append(p.val)
            p = p.next
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

n = Node("a")
n.next = Node("b")
n.next.next = Node("c")
n.next.next.next = Node("b")
n.next.next.next.next = Node("a")
l = LinkedList(n)
print(l.is_palindrome())
