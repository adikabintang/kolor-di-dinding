class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return "val: " + str(self.val)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

def is_child(parent: Node, node: Node):
    if parent is None:
        return False
    
    if parent == node:
        return True

    r = is_child(parent.left, node)
    if r:
        return r
    else:    
        return is_child(parent.right, node)

def get_first_comm_ancestor_helper(root: Node, p: Node, q: Node) -> Node:
    if is_child(root, p) == False or is_child(root, q) == False:
        return None
    
    return get_first_comm_ancestor(root, p, q)

def get_first_comm_ancestor(root: Node, p: Node, q: Node) -> Node:
    if root is None or p == root or q == root:
        return root
    
    is_p_on_left = is_child(root.left, p)
    is_q_on_left = is_child(root.left, q)

    if is_p_on_left != is_q_on_left:
        return root
    
    if is_p_on_left and is_q_on_left:
        return get_first_comm_ancestor(root.left, p, q)
    else:
        return get_first_comm_ancestor(root.right, p, q)

n = Node(20)
n.left = Node(10)
n.right = Node(30)
n.left.left = Node(5)
n.left.right = Node(15)
q = Node(17)
n.left.right.right = q
p = Node(3)
n.left.left.left = p
n.left.left.right = Node(7)
bt = BinaryTree(n)
print(get_first_comm_ancestor_helper(n, p, q))
