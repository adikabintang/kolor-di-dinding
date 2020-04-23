# https://leetcode.com/problems/most-common-word/
# Runtime: 36 ms, faster than 39.42% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions 
# time complexity: O(n + m), n is the number of words in the paragraph, 
#   m is the length of banned list
# space complexity: O(n + m), same as above
class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        import re
        regex = re.compile("[^a-zA-Z]")
        word_ctr = {}
        for word in regex.sub(" ", paragraph).split():
            word_small = word.lower()
            if word_small in word_ctr:
                word_ctr[word_small] += 1
            else:
                word_ctr[word_small] = 1
        
        banned_set = set(banned)
        maxi = 0
        result = ""
        for word, counter in word_ctr.items():
            if word not in banned_set:
                if counter > maxi:
                    maxi = counter
                    result = word
                    
        return result