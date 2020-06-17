# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        last_checked = n
        while left < right:
            mid = (left + right) // 2
            bad = isBadVersion(mid)
            if bad:
                right = mid
            else:
                left = mid + 1
            if bad:
                last_checked = mid
        return last_checked
        