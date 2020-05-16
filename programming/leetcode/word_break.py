class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        word_set = set(wordDict)
        max_len = 0
        for word in word_set:
            max_len = max(max_len, len(word))
        j = 1
        while j <= len(s):
            temp = s[:j]
            if temp in word_set or s in word_set:
                s = s[len(temp if temp in word_set else s):]
                j = 0
            else:
                if j >= max_len:
                    return False
                j += 1
        
        return len(s) == 0
    
s = Solution()
#print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
#print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))