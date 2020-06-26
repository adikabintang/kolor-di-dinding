# https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        arr = []
        while num > 0:
            arr.insert(0, num % 10)
            num //= 10
        num = res
        for i in range(len(arr)):
            # math.prod(arr)
            j = i + 1
            for j in range(j, len(arr)):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                n = self.__arr_to_int(arr)
                if n > res:
                    res = n
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
        return res
    
    def __arr_to_int(self, arr: [int]) -> int:
        res = 0
        for n in arr:
            res = res * 10 + n
        return res

s = Solution()

assert s.maximumSwap(2736) == 7236
