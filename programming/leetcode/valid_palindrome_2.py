# https://leetcode.com/problems/valid-palindrome-ii/
# Runtime: 112 ms, faster than 72.05% of Python3 online submissions
# Memory Usage: 14.4 MB, less than 6.25% of Python3 online submissions
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(s[:i] + s[i+1:]) \
                    or self.is_palindrome(s[:j] + s[j+1:])
            i += 1
            j -= 1
        return True
    
    def is_palindrome(self, s):
        return s == s[::-1]
    
s = Solution()
print(s.validPalindrome("aba"))
