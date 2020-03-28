class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        v = 0
        if root:
            v += self.rangeSumBST(root.left, L, R)
            if root.val >= L and root.val <= R:
                v += root.val
            v += self.rangeSumBST(root.right, L, R)
        
        return v