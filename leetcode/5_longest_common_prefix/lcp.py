# 44 ms	
# 13.8 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = "" if len(strs) == 0 else strs[0]
        for i in range(1, len(strs)):
            loop = min(len(temp), len(strs[i]))
            k = loop
            for j in range(0, loop):
                if temp[j] != strs[i][j]:
                    k = j
                    break
            temp = temp[0:k]
        
        return temp
                