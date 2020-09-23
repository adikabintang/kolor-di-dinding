# https://leetcode.com/problems/group-shifted-strings/
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: [str]) -> [[str]]:
        groupped = defaultdict(list)
        for s in strings:
            pattern = tuple()
            for i in range(1, len(s)):
                pattern += ((ord(s[i]) - ord(s[i-1]) + 26) % 26, )
            groupped[pattern].append(s)
        return groupped.values()
