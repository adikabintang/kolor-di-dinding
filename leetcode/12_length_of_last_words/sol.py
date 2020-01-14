# Runtime: 24 ms, faster than 84.93% of Python3 online submissions
# Memory Usage: 13 MB, less than 98.25% of Python3 online submissions 
def lengthOfLastWord(s: str) -> int:
    arr = s.split()
    if len(arr) == 0:
        return 0
    else:
        return len(arr[-1])

print(lengthOfLastWord("Hello world"))
print(lengthOfLastWord(""))
print(lengthOfLastWord("Helloworld"))