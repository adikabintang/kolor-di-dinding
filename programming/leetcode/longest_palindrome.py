class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi = 0
        i = 0
        result_str = ""
        while i < len(s):
            p_len = 0
            j = len(s) - 1
            while j > i:
                if j - i < maxi:
                    break
                    
                if self.is_palindrome(s, i, j):
                    p_len = j - i
                    break
                j -=1
            if p_len >= maxi:
                maxi = p_len
                result_str = s[i:j+1]
                
            i += 1
            
        return result_str

    def is_palindrome(self, s: str, l: int, r: int):
        r0 = 0
        l1 = 0
        if (l + r) % 2 == 0:
            r0 = (l + r) // 2
            l1 = r0 + 1
        else:
            r0 = ((l+r) // 2) + 1
            l1 = r0
        s0 = s[l:r0]
        s1 = s[l1:r+1]
        return s1[::-1] == s0
        # iterating manually is much slower, even though the time complexity
        # might be the same
#         while l <= r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
            
#         return True

s = Solution()
print(s.longestPalindrome("abacdfgdcaba"))
