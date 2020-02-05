# 52 ms
# 15.2 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
        
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in d:
                if i != d.get(complement):
                    return [i, d.get(complement)]
        
        return []