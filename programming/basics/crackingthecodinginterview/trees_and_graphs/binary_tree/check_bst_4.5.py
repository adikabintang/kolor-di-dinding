class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
    
    def __str__(self):
        return str(self.val) + ", r: " + str(self.r.val) + ", l: " + str(self.l.val)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def __in_order(self, node_n, arr=None):
        if arr is None:
            arr = []
        
        if node_n:
            self.__in_order(node_n.l, arr)
            arr.append(node_n.val)
            self.__in_order(node_n.r, arr)
    
        return arr

    def validate_bst(self):
        arr = self.__in_order(self.root)
        print(arr)
        for i in range(1, len(arr) - 1):
            if arr[i-1] > arr[i] or arr[i+1] < arr[i]:
                return False
        
        return True
    
    def print(self):
        arr = self.__in_order(self.root)
        print(arr)

if __name__ == "__main__":
    bt = BinaryTree(Node(8))
    bt.root.l = Node(4)
    bt.root.r = Node(10)
    bt.root.r.r = Node(20)
    bt.root.l.l = Node(2)
    bt.root.l.r = Node(12)
    bt.print()
    print(bt.validate_bst())
    #print(bt.root)
