class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return
        
        prev = nums[length-1]
        for i in range(length - 2, -1, -1):
            if nums[i] < prev:
                j = i + 1
                while j < length and nums[j] > nums[i]:
                    j += 1
                j -= 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                nums[i+1:].sort(reverse=True)
                return
                
            prev = nums[i]

s = Solution()
arr = [1, 2, 3]
s.nextPermutation(arr)
assert arr == [1,3,2]
