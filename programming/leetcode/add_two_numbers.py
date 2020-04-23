# https://leetcode.com/problems/add-two-numbers/
# Runtime: 76 ms, faster than 33.67% of Python3 online submissions 
# Memory Usage: 14 MB, less than 5.67% of Python3 online submissions
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = 0
        y = 0
        l1_ptr = l1
        mult = 1
        while l1_ptr:
            x += l1_ptr.val * mult
            mult *= 10
            l1_ptr = l1_ptr.next
        
        mult = 1
        l2_ptr = l2
        while l2_ptr:
            y += l2_ptr.val * mult
            mult *= 10
            l2_ptr = l2_ptr.next
        
        res_int = x + y
        val = (res_int) % 10
        res_int = res_int // 10
        res = ListNode(val)
        res_ptr = res
        while res_int > 0:
            val = (res_int) % 10
            res_int = res_int // 10
            res_ptr.next = ListNode(val)
            res_ptr = res_ptr.next
        
        return res

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1, l2))
