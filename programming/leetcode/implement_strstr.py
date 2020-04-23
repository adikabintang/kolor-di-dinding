# https://leetcode.com/problems/implement-strstr/
# Runtime: 20 ms, faster than 97.94% of Python3 online submissions 
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
def strStr(haystack: str, needle: str):
    needle_len = len(needle)
    if needle_len == 0:
        return 0
    
    haystack_len = len(haystack)
    
    for i in range(0, haystack_len - needle_len + 1):
        if needle == haystack[i : i + needle_len]:
            return i
    
    return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))

haystack = "a"
needle = "a"
print(strStr(haystack, needle))
