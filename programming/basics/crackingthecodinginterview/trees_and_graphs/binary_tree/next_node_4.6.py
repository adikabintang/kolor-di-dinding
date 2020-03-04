class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return "val: " + str(self.val if self != None else "none")
        

class BinaryTree:
    def __init__(self):
        self.root = None
        self.flag = False
    
    def next_node(self, desired_node_val, root=None):
        found = None
        if root:
            found = self.next_node(desired_node_val, root.left)
            if found:
                return found
            
            if self.flag == True:
                self.flag = False
                return root
            else:
                if desired_node_val == root.val:
                    self.flag = True
                
                found = self.next_node(desired_node_val, root.right)
            
            if found:
                return found
            
        return found

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right = Node(3)
    bt.root.right.left = Node(0)
    bt.root.right.right = Node(9)

    t = [4, 2, 5, 1, 0, 3, 9]
    for e in t:
        print(bt.next_node(e, bt.root))
     