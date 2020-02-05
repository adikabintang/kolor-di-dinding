# runtime: 5440 ms
# memory: 14.8 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0, l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
