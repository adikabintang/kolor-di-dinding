# https://leetcode.com/problems/subarray-sum-equals-k/
# Runtime: 92 ms, faster than 99.96% of Python3 online submissions
# Memory Usage: 16 MB, less than 20.00% of Python3 online submissions
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        sum_freq = {}
        sum_freq[0] = 1
        s = 0
        for n in nums:
            s += n
            if (s - k) in sum_freq:
                total += sum_freq[s - k]
            if s in sum_freq:
                sum_freq[s] += 1
            else:
                sum_freq[s] = 1
                
        return total