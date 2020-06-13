# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        p_len = len(p)
        p_ctr = Counter(p)
        temp_ctr = None
        res = []
        for i in range(len(s) - p_len + 1):
            if not temp_ctr:
                temp_ctr = Counter(s[i : i + p_len])
            else:
                temp_ctr[s[i + p_len - 1]] += 1

            if p_ctr == temp_ctr:
                res.append(i)
            temp_ctr[s[i]] -= 1
            if temp_ctr[s[i]] == 0:
                del temp_ctr[s[i]]
        
        return res

s = Solution()
assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
assert s.findAnagrams("acdcaeccde", "c") == [1,3,6,7]
