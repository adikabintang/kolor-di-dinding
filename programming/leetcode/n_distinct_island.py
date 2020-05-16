# https://leetcode.com/problems/number-of-distinct-islands/
# Runtime: 228 ms, faster than 71.99% of Python3 online submissions
# Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions
class Solution:
    def numDistinctIslands(self, grid: [[int]]) -> int:
        all_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    s = frozenset(self.get_island_shape(grid, row, col, row, col))
                    all_islands.add(s)
        
        return len(all_islands)
    
    def get_island_shape(self, grid: [[int]], i, j, i0, j0, visited=None, \
        island_shape=None):
        
        if visited is None or island_shape is None:
            visited = set()
            island_shape = set()

        if (i, j) in visited or grid[i][j] == 0:
            return island_shape

        visited.add((i, j))
        island_shape.add((i - i0, j - j0))
        grid[i][j] = 0

        if j + 1 < len(grid[i]):
            island_shape = self.get_island_shape(grid, i, j + 1, i0, j0, visited, island_shape)
        
        if j - 1 >= 0:
            island_shape = self.get_island_shape(grid, i, j - 1, i0, j0, visited, island_shape)
        
        if i + 1 < len(grid):
            island_shape = self.get_island_shape(grid, i + 1, j, i0, j0, visited, island_shape)
        
        if i - 1 >= 0:
            island_shape = self.get_island_shape(grid, i - 1, j, i0, j0, visited, island_shape)
        
        return island_shape

s = Solution()
# arr = [
#     [0, 0, 0],
#     [0, 0, 1],
#     [0, 1, 1]
# ]
arr = [
    [1,1,0,1,1],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [1,1,0,1,1]
]
print(s.numDistinctIslands(arr))
