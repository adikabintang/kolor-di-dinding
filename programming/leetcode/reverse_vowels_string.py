# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = {"a", "i", "u", "e", "o"}
        res = list(s)
        while l < r:
            while (l < len(s) and 
                   (not s[l].isalpha() or s[l].lower() not in vowels)):
                l += 1
                
            while (r >= 0 and
                (not s[r].isalpha() or s[r].lower() not in vowels)):
                r -= 1
                    
            if l < r:
                temp = res[l]
                res[l] = res[r]
                res[r] = temp
                l += 1
                r -= 1
        return "".join(res)
