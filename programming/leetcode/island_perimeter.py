# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: [[]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        visited = set()
        
        per = 0
        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == 1:
                    per += self.__helper(grid, row, col, visited)
        return per
    
    def __helper(self, grid: [[int]], row: int, col: int, visited: set, 
        per: int = 0) -> int:
        
        n_row = len(grid)
        n_col = len(grid[0])
        
        if row < 0 or row >= n_row or col < 0 or col >= n_col \
            or grid[row][col] == 0:
            return per
        
        if ((row, col) not in visited):
            visited.add((row, col))
            sides = 4
            if row - 1 >= 0 and grid[row-1][col] == 1:
                sides -= 1
            if row + 1 < n_row and grid[row+1][col] == 1:
                sides -= 1
            if col - 1 >= 0 and grid[row][col-1] == 1:
                sides -= 1
            if col + 1 < n_col and grid[row][col+1] == 1:
                sides -= 1

            per += sides
            per = self.__helper(grid, row-1, col, visited, per)
            per = self.__helper(grid, row+1, col, visited, per)
            per = self.__helper(grid, row, col+1, visited, per)
            per = self.__helper(grid, row, col-1, visited, per)
        
        return per
        
s = Solution()

res = s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(res)
assert res == 16
