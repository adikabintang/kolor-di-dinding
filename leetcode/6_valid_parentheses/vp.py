# inget stack data structure kalo ketemu ginian
# 36 ms
# 14 MB
class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        stack = list(s)
        stack_size = 0
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack[stack_size] = c
                stack_size += 1
            else:
                if stack_size > 0:
                    if (c == ']' and stack[stack_size - 1] == '[') or \
                            (c == ')' and stack[stack_size - 1] == '(') or \
                            (c == '}' and stack[stack_size - 1] == '{'):
                        stack_size -= 1
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
        
        return True if (stack_size == 0 and result == True) else False