# Runtime: 32 ms, faster than 85.25% of Python3 online submissions
# Memory Usage: 14 MB, less than 7.69% of Python3 online submissions 
class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        letter_logs = []
        digit_logs = []
        for line in logs:
            if line.split()[1].isalpha():
                letter_logs.append(line)
            else:
                digit_logs.append(line)
            
        letter_logs.sort(key=lambda s: (s.split(" ", 1)[1], s.split(" ", 1)[0]))
        result = letter_logs
        
        result.extend(digit_logs)
        return result
    
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
s = Solution()
print(s.reorderLogFiles(logs))
