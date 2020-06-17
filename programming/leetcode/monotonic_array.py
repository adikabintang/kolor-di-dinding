# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        a_len = len(A)
        prev = A[0] if a_len > 0 else 0
        is_decided = False
        up = False
        for i in range(1, a_len):
            if is_decided == False:
                if A[i] < prev:
                    up = False
                    is_decided = True
                if A[i] > prev:
                    up = True
                    is_decided = True
                prev = A[i]
                continue
            else:
                if A[i] < prev and up:
                    return False
                if A[i] > prev and up == False:
                    return False
                prev = A[i]
        
        return True
