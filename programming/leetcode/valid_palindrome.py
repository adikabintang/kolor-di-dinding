# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join(c.lower() for c in s if c.isalnum())
        return temp == temp[::-1]