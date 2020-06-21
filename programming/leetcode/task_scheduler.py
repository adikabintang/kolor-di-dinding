# https://leetcode.com/problems/task-scheduler/

from collections import Counter

class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        task_ctr = Counter(tasks)
        intervals = 0
        all_tasks = [k for k, _ in task_ctr.items()]
        
        for i in range(len(all_tasks)):
            task = all_tasks[i]
            jump = 1
            while task_ctr[task] > 0:
                task_ctr[task] -= 1
                intervals += 1
                # if task_ctr[task] <= 0:
                #     break
                
                if i + jump >= len(all_tasks):
                    jump = 1
                j = i + jump
                jump += 1
                ctr = 0
                while j < len(all_tasks) and ctr < n:
                    if task_ctr[all_tasks[j]] > 0:
                        task_ctr[all_tasks[j]] -= 1
                        intervals += 1
                        ctr += 1
                    j += 1

                if task_ctr[all_tasks[i]] > 0:  
                    intervals += (n - ctr)
        return intervals

s = Solution()
arr = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I",
    "J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S",
    "S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]
assert s.leastInterval(arr, 2) == 52
arr = ["A","A","B","B","C","C", "D", "D"]
assert s.leastInterval(arr, 2) == 8
assert s.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert s.leastInterval(["A", "A", "A", "B"], 2) == 7