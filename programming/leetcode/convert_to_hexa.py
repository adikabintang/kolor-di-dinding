# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
class Solution:
    def toHex(self, num: int) -> str:
        s = ""
        if num < 0:
            num = (0xffffffff - abs(num)) + 1
            
        while num >= 0:
            # 26 = 1 * 16 ^ 1 + 10 * 16 ^ 0
            n = num % 16
            if n > 9:
                s = chr((n-10)+ord("a")) + s
            else:
                s = str(n) + s
            num //= 16
            if num == 0:
                break
        
        return s

s = Solution()
assert s.toHex(-1) == "ffffffff"
assert s.toHex(26) == "1a"
