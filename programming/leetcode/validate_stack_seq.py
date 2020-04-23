# https://leetcode.com/problems/validate-stack-sequences/
# Runtime: 80 ms, faster than 19.92% of Python3 online submissions 
# Memory Usage: 14.1 MB, less than 20.00% of Python3 online submissions 
# Runtime: O(N)
# Memory: O(N)
class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        stack = []
        i = 0
        while i < len(pushed) and len(popped) > 0:
            popped_front = popped[0]
            while i < len(pushed):
                stack.append(pushed[i])
                i += 1
                if stack[-1] == popped_front:
                    break
            
            while len(stack) > 0 and len(popped) > 0:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    break
        
        return len(stack) == 0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

# pushed = [1,2,3,4,5]
# popped = [4,3,5,1,2]
s = Solution()
print(s.validateStackSequences(pushed, popped))
