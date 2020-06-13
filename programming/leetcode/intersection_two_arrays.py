# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        deleted_keys = []
        for k, v in c1.items():
            if k not in c2:
                deleted_keys.append(k)
            else:
                c1[k] = min(c1[k], c2[k])
        
        for k in deleted_keys:
            del c1[k]
            
        res = []
        for k, v in c1.items():
            res.extend([k] * v)
            
        return res
