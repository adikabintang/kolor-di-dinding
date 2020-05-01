# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        pq = []
        intervals.sort(key = lambda x: x[0])
        if len(intervals) > 0:
            pq.append(intervals[0][1])
        
        i = 1
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            if start >= pq[0]:
                pq[0] = end
                self.adjust_down_min_heap(pq)
            else:
                pq.append(end)
                self.adjust_up_min_heap(pq)
            i += 1
        
        return len(pq)
    
    def adjust_down_min_heap(self, pq):
        l = 1
        r = 2
        i = 0
        while i < len(pq) and l < len(pq) or r < len(pq):
            smallest_i = 0
            if l < len(pq) and r < len(pq):
                smallest_i = l if pq[l] < pq[r] else r
            else:
                smallest_i = l if l < len(pq) else r
            if pq[i] > pq[smallest_i]:
                temp = pq[i]
                pq[i] = pq[smallest_i]
                pq[smallest_i] = temp
                i = smallest_i
                l = 2 * i + 1
                r = 2 * i + 2
            else:
                break
    
    def adjust_up_min_heap(self, pq):
        i = len(pq) - 1
        parent = i // 2
        while parent >= 0 and pq[i] < pq[parent]:
            temp = pq[i]
            pq[i] = pq[parent]
            pq[parent] = temp
            i = parent
            parent = i // 2

arr = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
s = Solution()
print(s.minMeetingRooms(arr))
