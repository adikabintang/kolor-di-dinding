# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        n_cols = len(matrix[0])
        n_rows = len(matrix)
        start_row = 0
        end_row = n_rows - 1
        
        while start_row < end_row:
            m = (start_row + end_row) // 2
            if target > matrix[m][n_cols-1]:
                start_row = m + 1
                continue
            
            if target < matrix[m][0]:
                end_row = m - 1
                continue
            
            if target > matrix[start_row][n_cols-1]:
                start_row += 1
                continue
            
            if target < matrix[end_row][0]:
                end_row -= 1
                continue
            
            break
        
        i = start_row
        while i <= end_row:
            if len(matrix[i]) > 0:
                if self.binary_search(matrix[i], n_cols, target):
                    return True
            i += 1
        return False       
        
    def binary_search(self, arr, n_cols, target):
        l = 0
        r = n_cols - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            if target > arr[m]:
                l = m + 1
            else:
                r = m - 1
        return False
        
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
#m = [[5]]
m = [[]]
s = Solution()
print(s.searchMatrix(m, 5))
