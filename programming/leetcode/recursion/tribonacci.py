# https://leetcode.com/problems/n-th-tribonacci-number/
class SolutionWithDecorator:
    def memoize(self, func):
        memo = {}
        def helper(n: int):
            if n not in memo:
                memo[n] = func(n)
            return memo[n]
        return helper

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

class Solution:
    # with memoization
    # Runtime: 28 ms, faster than 57.65%
    # Memory Usage: 12.8 MB, less than 100.00%
    def memoization(self, n: int, arr=None) -> int:
        if arr is None:
            arr = [0] * ((n+1) if n > 2 else 3) 
            arr[1] = 1
            arr[2] = 1
        
        if arr[n] == 0 and n >= 3:
            arr[n] = self.memoization(n - 1, arr) + \
                self.memoization(n - 2, arr) + self.memoization(n - 3, arr) 

        return arr[n]

    def trib(self, n: int) -> int:
        return self.memoization(n)   

    # timeout, may need memoization
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

# faster, but too verbose
# Runtime: 24 ms, faster than 84.15% 
# Memory Usage: 12.7 MB, less than 100.00%
class SolutionLoop:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        d = a + b + c
        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return a + b
        elif n == 3:
            return a + b + c 
        
        for i in range(3, n):
            a = b
            b = c
            c = d
            d = a + b + c
        
        
        return d

if __name__ == "__main__":
    s = Solution()
    n = 4
    import time
    t0 = int(round(time.time() * 1000))
    t = s.tribonacci(n)
    t1 = int(round(time.time() * 1000))
    print("tribonacci: %d, time: %d" % (t, t1-t0))
    t0 = int(round(time.time() * 1000))
    t = s.trib(n)
    t1 = int(round(time.time() * 1000))
    print("memoization: %d, time: %d" % (t, t1-t0))

    # sd = SolutionWithDecorator()
    # trib = sd.memoize(sd.tribonacci)
    # t0 = int(round(time.time() * 1000))
    # t = trib(n)
    # t = trib(n)
    # t1 = int(round(time.time() * 1000))
    # print("memoization with decorator: %d, time: %d" % (t, t1 - t0))
