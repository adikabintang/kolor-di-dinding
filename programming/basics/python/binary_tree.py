class Node:
    def __init__(self, data=None, Node=None):
        self.data = data
        self.right = None
        self.left = None
    
    # like toString() of Java
    def __repr__(self):
        return str(self.data)

def insert(node: Node, data):
    if node:
        if data > node.data:
            if node.right:
                insert(node.right, data)
            else:
                node.right = Node(data)
        else:
            if node.left:
                insert(node.left, data)
            else:
                node.left = Node(data)
    
def in_order_traversal(node: Node):
    if node:
        in_order_traversal(node.left)
        print(node)
        in_order_traversal(node.right)

root = Node(4)
insert(root, 3)
insert(root, 7)
insert(root, 0)
# root = Node(4)
# l = Node(3)
# r = Node(7)
# o = Node(0)
# root.left = l
# root.right = r
# root.left.left = o
in_order_traversal(root)
