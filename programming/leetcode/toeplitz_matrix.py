# https://leetcode.com/problems/toeplitz-matrix/
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        
        for i in range(n_row):
            row = i
            col = 0
            prev = matrix[row][col]
            while row < n_row and col < n_col:
                if matrix[row][col] != prev:
                    return False
                row += 1
                col += 1
        
        for i in range(1,n_col):
            row = 0
            col = i
            prev = matrix[row][col]
            while col < n_col and row < n_row:
                if matrix[row][col] != prev:
                    return False
                row += 1
                col += 1
        
        return True
