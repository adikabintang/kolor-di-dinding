# https://leetcode.com/problems/meeting-rooms-ii/
# Runtime: 76 ms, faster than 83.27% of Python3 online submissions
# Memory Usage: 17 MB, less than 5.41% of Python3 online submissions 
import heapq

class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if len(intervals) == 0:
            return 0
        pq = []
        intervals.sort(key=lambda x: x[0])
        for m in intervals:
            start = m[0]
            end = m[1]
            if len(pq) == 0:
                pq.append(end)
            else:
                if start >= pq[0]:
                    heapq.heappop(pq)
                heapq.heappush(pq, end)
        return len(pq)


arr = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
s = Solution()
print(s.minMeetingRooms(arr))
