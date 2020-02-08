def compress(s: str):
    result_string = ""

    i = 0
    while i < len(s):
        buff = s[i]
        counter = 0
        while buff == s[i]:
            counter += 1
            i += 1
            if i >= len(s):
                break
        
        result_string += (buff + str(counter))
    
    if len(result_string) >= len(s):
        return s
    else:
        return result_string

s = "aabcccccaaa"
print(compress(s))
s = "abc"
print(compress(s))
