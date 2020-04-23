# 76 ms
# 14.1 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        l = list(s)
        panjang = len(l)
        r = True
        for i in range(0, panjang // 2):
            if l[i] != l[panjang - 1 - i]:
                r = False
        
        return r