class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, n):
        if n is None:
            return -1
        
        return max(self.get_height(n.left), self.get_height(n.right)) + 1
    
    def check_balance(self):
        s = self.__get_depths_as_set(self.root)
        return True if len(s) <= 2 else False
    
    def __get_depths_as_set(self, node_n, depth=0, depth_set=None):
        if depth_set is None:
            depth_set = set()
        
        if node_n:
            depth_set = self.__get_depths_as_set(node_n.left, depth+1, depth_set)
            depth_set = self.__get_depths_as_set(node_n.right, depth+1, depth_set)
            return depth_set
        else:
            depth -= 1
            depth_set.add(depth)
            return depth_set

root = Node(6)
bt = BinaryTree()
bt.root = root
bt.root.left = Node(3)
bt.root.left.left = Node(1)
bt.root.left.left.left = Node(0)
bt.root.left.right = Node(4)
bt.root.left.left.right = Node(2)
bt.root.right = Node(8)
bt.root.right.left = Node(7)
bt.root.right.right = Node(9)

s = bt.check_balance()
print(s)
