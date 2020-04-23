# https://leetcode.com/problems/search-suggestions-system/
# Runtime: 376 ms, faster than 28.88% of Python3 online submissions
# Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions
# important lesson:
# this is the fastest thing I can come up with, in less than 3 minutes. Although
# I believe it should use "tries", it's better to come up with an unoptimal answer
# first to make sure we submit something within the time limit.
class Solution:
    def suggestedProducts(self, products: [str], searchWord: str) -> [[str]]:
        products.sort()
        res = []
        for i in range(1, len(searchWord)+1):
            s = searchWord[:i]
            arr = self.get_all_prefix(products, s)
            l = 3 if len(arr) > 3 else len(arr)
            res.append(arr[:l])
        return res
            
    
    def get_all_prefix(self, arr, prefix):
        res = []
        for word in arr:
            if word[:len(prefix)] == prefix:
                res.append(word)
            if word[:len(prefix)] > prefix:
                break
        return res