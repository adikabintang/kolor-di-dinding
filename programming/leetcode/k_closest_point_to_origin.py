# https://leetcode.com/problems/k-closest-points-to-origin/
# Runtime: 664 ms, faster than 93.00% of Python3 online submissions 
# Memory Usage: 19.1 MB, less than 5.80% of Python3 online submissions
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:K]
        