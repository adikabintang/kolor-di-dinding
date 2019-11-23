# Runtime: 84 ms, faster than 96.18% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        if len(nums) > 0:
            temp = nums[0]
            count += 1
            for n in nums[1:]:
                if temp != n:
                    temp = n
                    nums[count] = n
                    count += 1
            
        return count
            
        