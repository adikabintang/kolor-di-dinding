# 96 ms
# 14 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        divider = 1
        result = 0
        while x // divider != 0:
            result = result * 10 + x // divider % 10
            divider *= 10
        
        return True if x == result else False