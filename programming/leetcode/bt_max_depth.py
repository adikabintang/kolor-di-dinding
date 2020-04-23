# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxi = self.traverse(root, 0, 0)
        return maxi
    
    def traverse(self, root: TreeNode, ctr: int, maxi: int):
        if root is None:
            return ctr
        
        ctr += 1
        n = self.traverse(root.left, ctr, maxi)
        maxi = max(n, maxi)
        n = self.traverse(root.right, ctr, maxi)
        maxi = max(n, maxi)
        
        return maxi
    