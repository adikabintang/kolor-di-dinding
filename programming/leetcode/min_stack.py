# https://leetcode.com/problems/min-stack/
from collections import namedtuple

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.El = namedtuple('El',['val','minimum']) 
        self.pos = -1
        
    def push(self, x: int) -> None:
        element = None
        if self.pos == -1 or x < self.nums[self.pos].minimum:
            element = self.El(x, x)
        else:
            element = self.El(x, self.nums[self.pos].minimum)
        self.nums.append(element)
        self.pos += 1
        
    def pop(self) -> None:
        self.nums.pop()
        self.pos -= 1

    def top(self) -> int:
        return self.nums[-1].val

    def getMin(self) -> int:
        return self.nums[-1].minimum
