# 4.2 page 109
# minimal tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.val)
            self.in_order_traversal(node.right)

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1

    def insert(self, val):
        p = self.root
        
        if p is None:
            p = Node(val)
            return

        while p.right and p.left:
            if val > p.val:
                p = p.right
            else:
                p = p.left
        
        if val > p.val:
            if p.right is None:
                p.right = Node(val)
            else:
                p.left.val = p.val
                if val > p.right.val:
                    p.val = p.right.val
                    p.right.val = val
                else:
                    p.val = val
        else:
            if p.left is None:
                p.left = Node(val)
            else:
                p.right.val = p.val
                if val < p.left.val:
                    p.val = p.left.val
                    p.left.val = val
                else:
                    p.val = val

arr = [1, 2, 3, 4, 5]
tree = Tree()

for a in arr:
    tree.insert(a)

print(tree.get_height(tree.get_root()))
