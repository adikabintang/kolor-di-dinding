# https://leetcode.com/problems/verifying-an-alien-dictionary/
# Runtime: 28 ms, faster than 93.19% of Python3 online submissions 
# Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions
class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        n = len(words)
        if n == 1 or n == 0:
            return True
        
        order_idx = {}
        i = 0
        for s in order:
            order_idx[s] = i
            i += 1
        
        i = 0
        char_idx = -1
        while i < n:            
            if order_idx[words[i][0]] < char_idx:
                return False
            
            if order_idx[words[i][0]] == char_idx:
                prev = i - 1
                prev_len = len(words[prev])
                cur_len = len(words[i])
                j = 0
                mini = min(prev_len, cur_len)
                while j < mini:
                    if order_idx[words[i][j]] < order_idx[words[prev][j]]:
                        return False
                    j += 1
                    prev_len -= 1
                    cur_len -= 1
                
                if prev_len > cur_len:
                    return False
            
            char_idx = order_idx[words[i][0]]
            i += 1
        
        return True

s = Solution()
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))