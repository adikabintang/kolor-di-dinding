# https://leetcode.com/problems/add-strings/
# Runtime: 52 ms, faster than 28.38% of Python3 online submissions 
# Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            gap = len(num1) - len(num2)
            pad = "0" * gap
            num2 = pad + num2
        elif len(num1) < len(num2):
            num1 = "0" * (len(num2) - len(num1)) + num1
        
        res = ""
        temp = 0
        for i in range(len(num1)-1, -1, -1):
            n = (temp + int(num1[i]) + int(num2[i])) % 10
            temp = (temp + int(num1[i]) + int(num2[i])) // 10
            res = str(n) + res
        
        if temp != 0:
            res = str(temp) + res
        
        return res

s = Solution()
print(s.addStrings("123", "678"))