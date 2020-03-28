class LinkedList:
    def __init__(self):
        self.val = 0
        self.next = None

def sum_lists_reversed(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    n1 = 0
    mult = 1
    l = ll1
    while l is not None:
        n1 = n1 + mult * l.val
        mult *= 10
        l = l.next
    
    n2 = 0
    mult = 1
    l = ll2
    while l is not None:
        n2 = n2 + mult * l.val
        mult *= 10
        l = l.next

    r = n1 + n2
    divider = 1
    res_list = LinkedList()
    l = res_list
    while r // divider != 0:
        l.val = (r // divider) % 10
        divider *= 10
        if r // divider != 0:
            l.next = LinkedList()
        l = l.next
    
    return res_list

def sum_lists_forward(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    n1 = 0
    l_ptr = ll1
    while l_ptr is not None:
        n1 = n1 * 10 + l_ptr.val
        l_ptr = l_ptr.next
    
    n2 = 0
    l_ptr = ll2
    while l_ptr is not None:
        n2 = n2 * 10 + l_ptr.val
        l_ptr = l_ptr.next

    r = n1 + n2
    divider = 1
    res_list = LinkedList()
    l_ptr = res_list
    while r // divider != 0:
        d = (r // divider) % 10
        if divider == 1:
            l_ptr.val = d
            res_list = l_ptr
        else:
            new_head = LinkedList()
            new_head.val = d
            new_head.next = res_list
            res_list = new_head
        divider *= 10
    
    return res_list

def print_ll(l: LinkedList):
    l_ptr = l
    while l_ptr is not None:
        print("%d -> " % l_ptr.val, end=""),
        l_ptr = l_ptr.next
    
    print("null")

l1 = LinkedList()
l1.val = 7
l1.next = LinkedList()
l1.next.val = 1
l1.next.next = LinkedList()
l1.next.next.val = 6

l2 = LinkedList()
l2.val = 5
l2.next = LinkedList()
l2.next.val = 9
l2.next.next = LinkedList()
l2.next.next.val = 2

# print_ll(l1)
# print("---")

print_ll(sum_lists_reversed(l1, l2))
print("---")
print_ll(sum_lists_forward(l1, l2))
