from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        ctr = Counter(S)
        seq = []
        
        for c, n in ctr.items():
            if n > (len(S) + 1) // 2:
                return ""
            seq.extend([c] * n)
        
        print(seq)
        res = [None] * len(S)
        j = 0
        for i in range(len(S), 2):
            res[i] = seq[j]
            print("%d: %s" % (j, seq[j]))
            j += 1
        j = len(S) // 2
        for i in range(1, len(S), 2):
            res[i] = seq[j]
            j += 1
        
        
#         res[::2] = seq[:len(S) // 2 + 1]
#         res[1::2] = seq[len(S) // 2:]
        print(res)
        return "".join(res)
            
s = Solution()
assert s.reorganizeString("aab") == "aba"
