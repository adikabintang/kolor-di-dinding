# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        digit = 0
        while n > 0:
            if n % 26 == 0:
                digit = 26 - 1
                n -= 1
            else:
                digit = n % 26 - 1
            col = chr(digit + ord("A"))
            res = col + res
            n //= 26
        return res