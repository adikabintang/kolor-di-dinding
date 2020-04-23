# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/solution/
class Solution:
    def minDominoRotations(self, A: [int], B: [int]) -> int:
        def check(x):
            rotations_a = 0
            rotations_b = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1
                
                if A[i] != x:
                    rotations_a += 1
                
                if B[i] != x:
                    rotations_b += 1
            
            return min(rotations_a, rotations_b)

        rotations = check(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return check(B[0])

        

    # Runtime: 1220 ms, faster than 54.74% of Python3 online submissions
    # Memory Usage: 14.6 MB, less than 14.29% of Python3 online submissions
    def minDominoRotationsV0(self, A: [int], B: [int]) -> int:
        number_flip_A = {}
        
        a_idx = -1
        for a in A:
            a_idx += 1
            if a not in number_flip_A:
                number_flip_A[a] = 0
                counter = 0
                for i in range(len(B)):
                    if A[i] == a:
                        counter += 1
                    else:                        
                        if B[i] == a:
                            number_flip_A[a] += 1
                            counter += 1
                        else:
                            break
                
                if counter != len(A):
                    number_flip_A[a] = -1
        
        number_flip_B = {}
        b_idx = -1
        for b in B:
            b_idx += 1
            if b not in number_flip_B:
                number_flip_B[b] = 0
                counter = 0
                for i in range(len(A)):
                    if B[i] == b:
                        counter += 1
                    else:
                        if A[i] == b:
                            number_flip_B[b] += 1
                            counter += 1
                        else:
                            break
                    
                if counter < len(B):
                    number_flip_B[b] = -1
        
        mini = len(A)
        a_possible = False
        for _, v in number_flip_A.items():
            if v != -1:
                a_possible = True 
                if v < mini:
                    mini = v
        
        b_possible = False
        for _, v in number_flip_B.items():
            if v != -1:
                b_possible = True
                if v < mini:
                    mini = v
        
        if a_possible == False and b_possible == False:
            return -1
        
        return mini       
        

s = Solution()
arr_1 = [2,1,2,4,2,2]
arr_2 = [5,2,6,2,3,2]
print(s.minDominoRotations(arr_1, arr_2))
