# Runtime: 32 ms, faster than 92.44% of Python3 online submissions 
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ori_len = len(nums)
        i = 0
        while i < ori_len:
            if nums[i] == val:
                counter = 1
                j = i + 1
                while j < ori_len:
                    if nums[j] != val:
                        break
                    j += 1
                    counter += 1
                    
                p = i
                while j < ori_len:
                    nums[p] = nums[j]
                    j += 1
                    p += 1
                i += 1
                ori_len -= counter
            else:
                i += 1
                
        return ori_len