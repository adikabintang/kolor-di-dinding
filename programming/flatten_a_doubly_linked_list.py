# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
# Runtime: 48 ms, faster than 15.50% of Python3 online submissions (-_-')
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions (o_o)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ptr = head
        while ptr:
            if ptr.child is not None:
                n = ptr.next
                the_next = self.flatten(ptr.child)
                the_next.prev = ptr
                ptr.next = the_next
                ptr.child = None
                p = ptr
                while p.next:
                    p = p.next
                if n:
                    n.prev = p
                    p.next = n
            ptr = ptr.next
        
        return head
        