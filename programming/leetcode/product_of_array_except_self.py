# https://leetcode.com/problems/product-of-array-except-self/
# Runtime: 5236 ms, faster than 5.14% of Python3 online submission
# Memory Usage: 20.6 MB, less than 48.00% of Python3 online submissions
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            n = nums[i - 1] * left[i - 1]
            left.append(n)
        
        right = [1]
        r_idx = -1
        for i in range(len(nums) - 1, 0, -1):
            n = nums[i] * right[r_idx]
            r_idx -= 1
            right = [n] + right
        
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        
        return res
        