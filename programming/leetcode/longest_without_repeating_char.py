# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        uniq = set()
        i = 0
        j = 0
        while i < len(s):
            while j < len(s) and s[j] not in uniq:
                uniq.add(s[j])
                j += 1
            maxi = max(maxi, len(uniq))
            if s[j - 1] in uniq:
                uniq.remove(s[i])
                i += 1
            
        return maxi

s = Solution()
print(s.lengthOfLongestSubstring("aabaab!bb"))
