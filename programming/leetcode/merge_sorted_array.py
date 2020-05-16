# https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        tail = len(nums1) - 1
        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[tail] = nums2[j]
                tail -= 1
                j -= 1
            else:
                nums1[tail] = nums1[i]
                tail -= 1
                i -= 1
        
        while j >= 0:
            nums1[tail] = nums2[j]
            j -= 1
            tail -= 1