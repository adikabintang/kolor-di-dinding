# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        paths = set()
        self.helper(root, paths)
        return list(paths)
    
    def helper(self, root: TreeNode, all_paths, path = ""):
        if not root:
            return path
        
        if path == "":
            path = str(root.val)
        else:
            path += "->" + str(root.val)

        p1 = self.helper(root.left, all_paths, path)
        if p1 and root.left is None and root.right is None:
            all_paths.add(p1)
        
        p2 = self.helper(root.right, all_paths, path)
        if p2 and root.left is None and root.right is None:
            all_paths.add(p2)

'''
   1
 /   \
2     3
 \
  5
'''
t = TreeNode(1)
t.left = TreeNode(2)
t.left.right = TreeNode(5)
t.right = TreeNode(3)

s = Solution()
print(s.binaryTreePaths(t))
