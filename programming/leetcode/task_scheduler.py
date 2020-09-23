# https://leetcode.com/problems/task-scheduler/

from collections import Counter

class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        freq.sort()
        f_max = freq.pop()
        idle_time = n * (f_max - 1)
        
        while freq and idle_time > 0:
            idle_time -= min(f_max - 1, freq.pop())
        
        idle_time = max(0, idle_time)
        
        return len(tasks) + idle_time

s = Solution()
arr = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I",
    "J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S",
    "S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]
assert s.leastInterval(arr, 2) == 52
arr = ["A","A","B","B","C","C", "D", "D"]
assert s.leastInterval(arr, 2) == 8
assert s.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert s.leastInterval(["A", "A", "A", "B"], 2) == 7