# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Runtime: 340 ms, faster than 5.14% of Python3 online submissions (-_-')
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions (o.o)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
        forest = set()
        forest.add(root)
        for val in to_delete:
            n = None
            parent = None
            for r in forest:
                n, parent = self.find_node(r, val)
                if n is not None:
                    break
            
            if n is not None:
                if n.right is not None:
                    forest.add(n.right)

                if n.left is not None:
                    forest.add(n.left)
                
                if n in forest:
                    forest.remove(n)
                
                if parent is None:
                    n = None
                else:
                    if parent.right is not None and parent.right.val == n.val:
                        parent.right = None
                    elif parent.left is not None and parent.left.val == n.val:
                        parent.left = None
                
        
        return list(forest)
    
    def find_node(self, root: TreeNode, val: int, parent=None) -> TreeNode:
        node = None
        if root:
            if root.val == val:
                return root, parent
            node, parent = self.find_node(root.left, val, root)
            if node is None:
                node, parent = self.find_node(root.right, val, root)
            
        return node, parent

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right = TreeNode(3)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)

s = Solution()
print(s.delNodes(t, [3, 5]))
