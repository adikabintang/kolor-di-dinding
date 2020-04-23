# https://leetcode.com/problems/rotting-oranges/
# Runtime: 48 ms, faster than 83.00% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 16.67% of Python3 online submissions
class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        n_rows = len(grid)
        if n_rows == 0:
            return 0
        
        q = [] # (row, column, depth)
        n_cols = len(grid[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        depth = 0
        while len(q) > 0:
            row, col, depth = q.pop(0)
            for r, c in self.__get_neighbors_point(grid, row, col):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    q.append((r, c, depth + 1))
        
        for row in grid:
            if 1 in row:
                return -1
        
        return depth

    def __get_neighbors_point(self, grid, i, j):
        points = []
        for row, col in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0:
                points.append((row, col))
        
        return points
    
arr = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
] #-1

#arr = [[2,1,1],[1,1,0],[0,1,1]] # 4
#arr = [[1,2]] # 1
#arr = [[1],[2]] # 1
#arr = [[0]] # 0
#arr = [[1,2,1,1,2,1,1]] # 2
#arr = [[2],[1],[1],[1],[2],[1],[1]] #2
#arr = [[2,2],[1,1],[0,0],[2,0]] #1
s = Solution()
print(s.orangesRotting(arr))
