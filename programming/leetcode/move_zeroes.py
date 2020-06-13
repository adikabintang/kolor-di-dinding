class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        ctr = 0
        while i < length:
            if ctr == length - 1:
                break
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
            else:
                i += 1
            ctr += 1

s = Solution()
assert s.moveZeroes([0,0,0,1]) == [1,0,0,0]
