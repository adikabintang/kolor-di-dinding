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
        s_arr = []
        t_arr = []
        self.tree_to_arr(s, s_arr)
        self.tree_to_arr(t, t_arr)
        return self.is_subarray(s_arr, t_arr)

    
    def tree_to_arr(self, root, arr):
        if root:
            arr.append(root.val)
            self.tree_to_arr(root.left, arr)
            self.tree_to_arr(root.right, arr)
        else:
            arr.append(None)
    
    def is_subarray(self, s, t):
        i = 0
        while i < len(s):
            if s[i] == t[0]:
                j = i
                k = 0
                r = True
                while j < len(s) and k < len(t):
                    if s[j] != t[k]:
                        r = False
                        break
                    j += 1
                    k += 1
                if r:
                    return True
            i += 1
        return False
                

        
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
