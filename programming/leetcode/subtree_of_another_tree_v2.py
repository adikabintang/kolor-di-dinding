# https://leetcode.com/problems/subtree-of-another-tree/
# important lesson:
# if we wanna compare subtree, we compare it from root, left, right.
# so, don't use in-order. use pre-order: root, left, right.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)
    
    def are_equal_nodes(self, s, t):
        if s is None and t is None:
            return True
        
        if s is None or t is None:
            return False
        
        return s.val == t.val and self.are_equal_nodes(s.left, t.left) and \
            self.are_equal_nodes(s.right, t.right)

    def traverse(self, s, t):
        # if s:
        #     if self.are_equal_nodes(s, t):
        #         return True
        #     res = self.traverse(s.left, t)
        #     if res:
        #         return True
        #     res = self.traverse(s.right, t)
        #     if res:
        #         return True

        # return False
        # same as
        return s and (self.are_equal_nodes(s, t) or self.traverse(s.left, t) or \
            self.traverse(s.right, t))
        
# s = TreeNode(3)
# s.left = TreeNode(4)
# s.right = TreeNode(5)
# s.left.left = TreeNode(1)
# s.left.left.left = TreeNode(0)
# s.left.right = TreeNode(2)

# t = TreeNode(4)
# t.left = TreeNode(1)
# t.right = TreeNode(2)

s = TreeNode(1)
s.left = TreeNode(2)
s.right = TreeNode(3)

t = TreeNode(2)
t.left = TreeNode(3)

sol = Solution()
print(sol.isSubtree(s, t))
