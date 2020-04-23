# https://leetcode.com/problems/maximal-square/
# Runtime: 364 ms, faster than 13.51% of Python3 online submissions
# Memory Usage: 14.5 MB, less than 9.09% of Python3 online submissions 
# very poor performance -_-
# time complexity: O((mn)^2), m = width, n = length
# space complexity: O(1)
class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        if len(matrix) == 0:
            return 0     
        
        maxi = 0
        i = 0
        j = 0
        while i < len(matrix):
            j = 0     
            while j < len(matrix[0]):
                if matrix[i][j] == "1":
                    maxi = max(maxi, self.get_square_area(matrix, i, j))
                j += 1
            i += 1
        
        return maxi
    
    def get_square_area(self, matrix, i, j):
        l = 1
        w = 1
        v = i
        h = j
        while v < len(matrix) and h < len(matrix[0]):
            if matrix[v][h] == "1":
                m = v
                flag = True
                while m >= i:
                    if matrix[m][h] != "1":
                        flag = False
                        break
                    m -= 1
                
                n = h
                while n >= j:
                    if matrix[v][n] != "1":
                        flag = False
                        break
                    n -= 1
                
                if flag == False:
                    break
            else:
                break
                                
            v += 1
            h += 1
        
        l = v - i
        w = h - j
                    
        return l * w
                 

matrix = [
    ["1","1","1","1"],
    ["1","1","1","1"],
    ["1","1","1","1"]
]

# matrix = [
#     ["0","0","0","1"],
#     ["1","1","0","1"],
#     ["1","1","1","1"],
#     ["0","1","1","1"],
#     ["0","1","1","1"]
# ]

# matrix = [
#     ["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","0","1","0"]
# ]

# matrix = [["0"]]

# matrix = [
#     ["1","1","0","1"],
#     ["1","1","0","1"],
#     ["1","1","1","1"]
# ]

# matrix = [
#     ["0"]
# ]

s = Solution()
print(s.maximalSquare(matrix))
