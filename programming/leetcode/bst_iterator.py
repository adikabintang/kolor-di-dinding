# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []
        self.i = 0
        self.__flatten(root, self.arr)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.arr[self.i]
        self.i += 1
        return n.val
    
    def __flatten(self, root: TreeNode, arr: [TreeNode]):
        if root:
            self.__flatten(root.left, arr)
            arr.append(root)
            self.__flatten(root.right, arr)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.i < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()