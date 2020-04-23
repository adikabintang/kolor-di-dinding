# https://leetcode.com/problems/merge-intervals/submissions/
class Solution:
    # Runtime: 176 ms, faster than 5.30% of Python3 online
    # Memory Usage: 15.5 MB, less than 6.52% of Python3 online submissions 
    def merge(self, intervals):
        i = 0
        res = []
        intervals.sort(key=lambda elem: elem[0])
        while i < len(intervals):
            mini = intervals[i][0]
            maxi = intervals[i][1]
            j = i + 1
            while j < len(intervals) and \
                maxi >= intervals[j][0] and mini <= intervals[j][1]:
                
                mini = min(mini, intervals[j][0])
                maxi = max(maxi, intervals[j][1])
                j += 1
            
            i = j
            res.append([mini, maxi])
            
        return res
            