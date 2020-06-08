from collections import Counter, OrderedDict

class Solution:
    def isok(self, s):
        i = 0
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                return False
            i += 1
            j += 1
        return True

    def reorganizeString(self, S: str) -> str:
        if self.isok(S):
            return S
            
        ctr = []
        for t in Counter(S).most_common():
            ctr.append([t[0], t[1]])

        s = ""
        print(ctr)
        i = 0
        j = i + 1
        while j < len(ctr):
            if ctr[i][1] <= 0:
                i = j
                j = i + 1
                if j >= len(ctr):
                    break
            while ctr[j][1] > 0:
                s += ctr[i][0] + ctr[j][0]
                ctr[j][1] -= 1
                ctr[i][1] -= 1
            j += 1

        if ctr[i][1] > 1:
            return ""
        s += ctr[i][0][:ctr[i][1]]
        return s

s = Solution()
# print(s.reorganizeString("vvlo"))
# print(s.reorganizeString("aaab"))
# print(s.reorganizeString("aab"))
# print(s.reorganizeString("cbaa"))
print(s.reorganizeString("bfrbs"))
