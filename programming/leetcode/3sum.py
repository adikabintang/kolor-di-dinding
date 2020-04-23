# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        el_index_map = {}
        res = set()
        for i in range(len(nums)):
            el_index_map[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = (nums[i] + nums[j]) * -1
                if target in el_index_map and el_index_map[target] > j:
                    res.add((nums[i], nums[j], target))
        
        return list(res)

# arr = [-1, 0, 1, 2, -1, -4]
arr = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
s = Solution()
print(s.threeSum(arr))
