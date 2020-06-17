# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.__helper(root, target, root.val)

    def __helper(self, root: TreeNode, target: float, closest: int = 0) -> int:
        if root:
            if abs(root.val - target) <= abs(closest - target):
                closest = root.val
                
            closest_left = self.__helper(root.left, target, closest)
            if abs(closest_left - target) < abs(closest - target):
                closest = closest_left
            
            closest_right = self.__helper(root.right, target, closest)
            if abs(closest_right - target) < abs(closest - target):
                closest = closest_right
            
        return closest

s = Solution()

t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(5)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
assert s.closestValue(t, 3.714) == 4

t = TreeNode(1)
t.right = TreeNode(2)
assert s.closestValue(t, 3.428571) == 2
