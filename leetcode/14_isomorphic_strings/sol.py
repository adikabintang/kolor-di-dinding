# Runtime: 32 ms, faster than 92.62% of Python3 online submissions
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
def isIsomorphic(s: str, t: str) -> bool:
    char_mapping = {}
    result = True
    t_index = 0
    for c in s:
        if c in char_mapping:
            if char_mapping[c] != t[t_index]:
                result = False
                break
        else:
            for k, v in char_mapping.items():
                if v == t[t_index]:
                    result = False
                    break
            char_mapping[c] = t[t_index]
        
        t_index += 1
    return result

s = "ab"
t = "aa"
print(isIsomorphic(s, t))

s = "egg"
t = "add"
print(isIsomorphic(s, t))

s = "foo"
t = "bar"
print(isIsomorphic(s, t))

s = "paper"
t = "title"
print(isIsomorphic(s, t))

s = ""
t = ""
print(isIsomorphic(s, t))