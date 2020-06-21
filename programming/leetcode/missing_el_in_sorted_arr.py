# https://leetcode.com/problems/missing-element-in-sorted-array/
class Solution:
    def missingElement(self, nums: [int], k: int) -> int:
        for i in range(len(nums) - 1):
            missing = nums[i + 1] - nums[i] - 1
            if k - missing > 0:
                k -= missing
            else:
                return nums[i] + k
        
        return nums[-1] + k

s = Solution()
assert s.missingElement([4,7,9,10], 1) == 5
assert s.missingElement([4,7,9,10], 3) == 8
assert s.missingElement([4,7,9,10], 2) == 6
assert s.missingElement([1,2,4], 6) == 9
