# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.temp = dict() # for memoization
        
    def climbStairs(self, n: int) -> int:
        # remember to meet the base case first no matter what, then continue
        # working
        if n <= 0:
            return 0
        if n <= 2:
            return n
        
        if n in self.temp:
            return self.temp[n]
        else:
            val = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.temp[n] = val
            return val
    