# https://leetcode.com/problems/sparse-matrix-multiplication/
class Solution:
    def multiply(self, A: [[int]], B: [[int]]) -> [[int]]:
        res = [[0] * len(B[0]) for i in range(len(A))]
        for row_res in range(len(res)):
            for col_res in range(len(res[0])):
                total = 0
                for el in range(len(B)):
                    total += A[row_res][el] * B[el][col_res]
                
                res[row_res][col_res] = total
            
        return res

s = Solution()
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

assert s.multiply(A, B) == [[7,0,0],[-7,0,3]]

A = [
    [1,-5]
]
B = [
    [12],
    [-1]
]

assert s.multiply(A, B) == [[17]]