# https://leetcode.com/problems/interval-list-intersections
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            a = A[i]
            b = B[j]
            lo = max(a[0], b[0])
            hi = min(a[1], b[1])
            if lo <= hi:
                res.append([lo, hi])
            
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
            
        return res
        