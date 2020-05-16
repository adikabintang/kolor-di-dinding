# https://leetcode.com/problems/add-binary/
# Runtime: 36 ms, faster than 40.21% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = 0
        res = ""
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
            
        for i in range(len(a) - 1, -1, -1):
            n = (temp + int(a[i]) + int(b[i])) % 2
            temp = (temp + int(a[i]) + int(b[i])) // 2
            res = str(n) + res
        
        if temp != 0:
            res = str(temp) + res
            
        return res
            