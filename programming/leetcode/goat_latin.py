# https://leetcode.com/problems/goat-latin/
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = {"a", "i", "u", "e", "o"}
        words = S.split()
        res = ""
        for i in range(len(words)):
            a = ["a"] * (i+1)
            ma = "ma" + "".join(a)
            if words[i][0].lower() in vowel:
                res += words[i] + ma
            else:
                res += words[i][1:] + words[i][0] + ma
            res += " "
        return res[:-1]
        