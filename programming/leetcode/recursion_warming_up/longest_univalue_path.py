# https://leetcode.com/problems/longest-univalue-path/
# binary tree, recursion


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max = 0
    
    def helper(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        arrow_left = 0
        arrow_right = 0
        if root.left:
            if root.left.val == root.val:
                arrow_left += left + 1
        
        if root.right:
            if root.right.val == root.val:
                arrow_right += right + 1
        
        if arrow_left + arrow_right > self.max:
            self.max = arrow_left + arrow_right
        
        return max(arrow_left, arrow_right)
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max = 0
        self.helper(root)
        return self.max

if __name__ == "__main__":
    s = Solution()

    bt = TreeNode(5)
    bt.left = TreeNode(4)
    bt.left.left = TreeNode(1)
    bt.left.right = TreeNode(1)
    bt.right = TreeNode(5)
    bt.right.right = TreeNode(5)
    print(s.longestUnivaluePath(bt))

    t = TreeNode(1)
    t.left = TreeNode(4)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(4)
    t.right = TreeNode(5)
    t.right.left = TreeNode(5)
    
    print(s.longestUnivaluePath(t))

    t = TreeNode(1)
    t.left = TreeNode(1)
    t.left.left = TreeNode(1)
    t.left.left.left = TreeNode(1)
    t.left.left.right = TreeNode(1)
    t.left.right = TreeNode(1)
    t.left.right.left = TreeNode(1)

    print(s.longestUnivaluePath(t))
