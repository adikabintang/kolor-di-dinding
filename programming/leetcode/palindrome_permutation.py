# https://leetcode.com/problems/palindrome-permutation
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_ctr = Counter(s)
        if len(s) % 2 == 0:
            if len(char_ctr) > len(s) // 2:
                return False
        else:
            if len(char_ctr) > len(s) // 2 + 1:
                return False
        
        odd_ctr = 0
        for _, v in char_ctr.items():
            if v % 2 != 0:
                odd_ctr += 1
            if odd_ctr > 1:
                return False
            
        return True
