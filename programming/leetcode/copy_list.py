# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __repr__(self):
        s = ""
        ptr = self
        while ptr:
            oi = "None"
            if ptr.random:
                oi = str(ptr.random.val)

            s += "(" + str(ptr.val) + ", " + oi + ") "
            ptr = ptr.next

        return s

class Solution:
    def get_idx(self, head, rand_node):
        if rand_node is None:
            return -1
            
        ptr = head
        i = -1
        while ptr:
            i += 1
            if ptr == rand_node:
                return i
            
            ptr = ptr.next
        
        return -1

    # Runtime: 80 ms, faster than 6.26% of Python3 online submissions 
    # Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions
    def copyRandomList(self, head: 'Node') -> 'Node':     
        res = None
        if head is None:
            return res
        
        res = Node(head.val)
        ptr_res = res
        ptr_in = head.next
        while ptr_in:
            ptr_res.next = Node(ptr_in.val)
            ptr_res = ptr_res.next
            ptr_in = ptr_in.next
        
        ptr_in = head
        ptr = res
        while ptr_in:
            random_idx = self.get_idx(head, ptr_in.random)
            if random_idx == -1:
                ptr.random = None
            else:
                p = res
                for _ in range(random_idx):
                    p = p.next
                ptr.random = p

            ptr = ptr.next
            ptr_in = ptr_in.next 
            
        return res
    
    def copyRandomListV2(self, head: 'Node') -> 'Node':
        res = None
        if head is None:
            return res
        
        res = Node(head.val)
        ptr_res = res
        ptr_in = head.next
        idx_rand = {}
        idx_rand[head] = res
        while ptr_in:
            ptr_res.next = Node(ptr_in.val)
            ptr_res = ptr_res.next
            idx_rand[ptr_in] = ptr_res
            ptr_in = ptr_in.next
        
        p = res
        ptr_in = head
        while p:
            if ptr_in.random in idx_rand:
                p.random = idx_rand[ptr_in.random]
            else:
                p.random = None
            p = p.next
            ptr_in = ptr_in.next
        
        return res

l = Node(1)
l.random = None
l.next = Node(2)
l.next.random = l
l.next.next = Node(3)
l.next.next.random = l.next

print(l)
s = Solution()
print("res:")
print(s.copyRandomListV2(l))
