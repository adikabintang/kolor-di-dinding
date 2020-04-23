# https://leetcode.com/problems/number-of-islands/
class Solution:
    # important to learn and remember here:
    # when doing DFS, just think like running in a maze and take every step
    # to go deeper
    def blusukan(self, grid, i, j):
        if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
            grid[i][j+1] = "0"
            self.blusukan(grid, i, j+1)
        
        if i < len(grid) - 1 and grid[i+1][j] == "1":
            grid[i+1][j] = "0"
            self.blusukan(grid, i+1, j)

        if j > 0 and grid[i][j-1] == "1":
            grid[i][j-1] = "0"
            self.blusukan(grid, i, j-1)
        
        if i > 0 and grid[i-1][j] == "1":
            grid[i-1][j] = "0"
            self.blusukan(grid, i-1, j)

    def numIslands(self, grid: [[str]]) -> int:
        v_len = len(grid)
        
        if v_len == 0:
            return 0

        h_len = len(grid[0])
        counter = 0
        i = 0
        while i < v_len:
            j = 0
            while j < h_len:
                if grid[i][j] == "1":
                    counter += 1
                    grid[i][j] = "0"
                    self.blusukan(grid, i, j)
                
                j += 1
            i += 1
                                
        return counter

arr = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]
s = Solution()
print(s.numIslands(arr))
