# https://leetcode.com/problems/top-k-frequent-words
# Runtime: 56 ms, faster than 63.24% of Python3 online submissions
# Memory Usage: 14 MB, less than 8.33% of Python3 online submissions
import collections
class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        # learn how to use collections.Counter
        # import collections
        # word_ctr = collections.Counter(words)
        word_ctr = {}
        for word in words:
            if word in word_ctr:
                word_ctr[word] += 1
            else:
                word_ctr[word] = 1
        
        word_sorted = sorted(word_ctr.items(), reverse=True, 
                             key=lambda item: item[1])
        same_range = []
        i = 0
        while i < len(word_sorted):
            freq0 = word_sorted[i][1]
            j = i
            while j < len(word_sorted) and freq0 == word_sorted[j][1]:
                j += 1
            if i != j:
                same_range.append((i, j))
                i = j
            else:
                i += 1
        
        for r in same_range:
            s = word_sorted[r[0]:r[1]]
            s.sort(key=lambda x: x[0])
            word_sorted[r[0]:r[1]] = s
        
        word_sorted = word_sorted[:k]
        
        res = [el[0] for el in word_sorted]
        return res
    
    def topKFrequentV1(self, words: [str], k: int) -> [str]:
        word_ctr = collections.Counter(words)
        u_word = word_ctr.keys()
        u_word.sort(key=lambda x: (-word_ctr[w], w))
        return u_word[:k]
        
