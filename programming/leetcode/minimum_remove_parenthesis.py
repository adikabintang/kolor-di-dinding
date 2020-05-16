# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Runtime: 124 ms, faster than 74.10% of Python3 online submissions 
# Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions
# remember: many parenthesis problems leverage stack to solve
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        res = s[:]
        while i < len(res):
            if res[i] == '(':
                stack.append(i)
            elif res[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    res = res[:i] + res[i+1:]
                    continue
            
            i += 1
                
        for i in range(len(stack)):
            res = res[:stack[i] - i] + res[stack[i] + 1 - i :]
        
        return res


s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))
print(s.minRemoveToMakeValid("())()((("))
