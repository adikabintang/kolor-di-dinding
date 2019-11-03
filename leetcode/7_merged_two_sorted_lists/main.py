# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 48 ms
# 13.8 MB
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = l1 if l1 is not None else l2
        it2 = l2 if result == l1 else l1
        head = result
        prev = result
        while it2 is not None:
            while result is not None and it2.val >= result.val:
                prev = result
                result = result.next
                    
            n = ListNode(it2.val)
            n.next = result
            if prev == result:
                head = n
                result = n
            else:
                prev.next = n
            prev = n
            it2 = it2.next
        
        return head