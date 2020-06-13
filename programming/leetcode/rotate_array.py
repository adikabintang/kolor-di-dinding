# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k %= nums_len
        temp = nums[nums_len-k:]
        i = nums_len - 1
        while i >= k:
            nums[i] = nums[i-k]
            i -= 1
        nums[:k] = temp[:]

s = Solution()
arr = [1,2,3,4,5,6,7]
s.rotate(arr, 3)
assert arr == [5,6,7,1,2,3,4]
