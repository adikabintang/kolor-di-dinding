# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        r = []
        self.helper(root, r)
        return r
    
    def helper(self, root: TreeNode, arr: [int], depth: int = 0):
        if root:
            depth += 1
            if len(arr) < depth:
                arr.append(root.val)
            self.helper(root.right, arr, depth)
            self.helper(root.left, arr, depth)
