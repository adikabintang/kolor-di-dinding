class Node:
    def __init__(self, name: str, children = None):
        self.name = name
        self.children = children

class Graph:
    def __init__(self, nodes: {str: Node} = None):
        self.nodes = nodes if nodes else {}
        self.temp_stack = []
        self.build_deps_set = set()
    
    def build_all(self):
        for _, node in self.nodes.items():
            if self.build(node) == False:
                return False
        
        return True
    
    def build(self, root):
        if root:
            if root.name in self.temp_stack:
                return False
            self.temp_stack.append(root.name)

            if root.children:
                for child in root.children:
                    if child.name not in self.build_deps_set:
                        if self.build(child) == False:
                            return False
                        else:
                            x = self.temp_stack.pop()
                            if x not in self.build_deps_set:
                                print(x)
                                self.build_deps_set.add(x)
            
            if len(self.temp_stack) > 0:
                x = self.temp_stack.pop()
                if x not in self.build_deps_set:
                    print(x)
                    self.build_deps_set.add(x)
    
        return True

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.children = [f]
# b.children = [f]
# c.children = [d]
# d.children = [a, b]

# g = Graph({"a": a, "b": b, "c": c, "d": d, "e": e, "f": f})
# g.build_all()

a = Node("a")
b = Node("b")
c = Node("c")

a.children = [b]
b.children = [c]
c.children = [a]

g = Graph({"a": a, "b": b, "c": c})
g.build_all()
