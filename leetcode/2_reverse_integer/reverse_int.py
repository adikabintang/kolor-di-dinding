# 32 ms
# 13.6 MB
class Solution:
    def reverse(self, x: int) -> int:
        divider = 1
        result = 0
        num = abs(x)
        while num // divider != 0:
            temp = num // divider % 10
            result = result * 10 + temp
            divider *= 10
            if result > 2 ** 31 - 1:
                return 0
        
        if x < 0:
            result = result * -1
        return result