# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Runtime: 32 ms, faster than 44.95% of Python3 online submissions 
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.arr = []
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.construct(root)
        m = self.arr[-1]
        for i in range(1, len(self.arr)):
            d = abs(self.arr[i] - self.arr[i-1])
            if d < m:
                m = d
        
        self.arr = None
        self.arr = []
        return m
    
    def construct(self, root: TreeNode):
        if root:
            self.construct(root.left)
            self.arr.append(root.val)
            self.construct(root.right)
            