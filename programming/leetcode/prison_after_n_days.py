# https://leetcode.com/problems/prison-cells-after-n-days/
class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        seen = {}
        while N > 0:
            cell_tuple = tuple(cells)
            if cell_tuple in seen:
                N = N % (seen[cell_tuple] - N)
            seen[cell_tuple] = N

            if N >= 1:
                N -= 1
                cells = [1 if i > 0 and i < len(cells)-1 and \
                     cells[i-1] == cells[i+1] else 0 \
                       for i in range(len(cells))]
        
        return cells

cells = [1,0,0,1,0,1,1,0]
N = 15
s = Solution()
print(s.prisonAfterNDays(cells, N))
