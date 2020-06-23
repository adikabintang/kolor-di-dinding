# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        ancestor = root
        if root == p or root == q:
            return ancestor

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            ancestor = root
        else:
            ancestor = left if left else right
        return ancestor

s = Solution()
t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)
t.left.left = TreeNode(6)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(7)
t.left.right.right = TreeNode(4)
t.right.left = TreeNode(0)
t.right.right = TreeNode(8)

# r = s.lowestCommonAncestor(t, t.left, t.right)
# assert r.val == 3

r = s.lowestCommonAncestor(t, t.left, t.left.right.right)
assert r.val == 5
