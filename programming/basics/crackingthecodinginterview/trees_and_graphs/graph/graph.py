class Node:
    def __init__(self, name=None, children=None):
        self.name = name
        self.children = children if children else []

    def __repr__(self):
        return str(str(self.name) + ": " + str(self.children))


class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes if nodes else []
        self.visited_nodes = {}

    def dfs(self, root):
        if root:
            print(root.name) # visit
            self.visited_nodes[root.name] = True
            for n in root.children:
                if self.visited_nodes.get(n.name) == None:
                    self.dfs(n)     
    
    def bfs(self, root):
        queue = []
        self.visited_nodes[root.name] = True
        queue.append(root)

        while queue:
            parent = queue.pop(0)
            print(parent.name) # visit
            for child in parent.children:
                if self.visited_nodes.get(child.name) == None:
                    self.visited_nodes[child.name] = True
                    queue.append(child)


nodes = [ Node(i) for i in range(6) ]
nodes[0].children = [nodes[1], nodes[4], nodes[5]]
nodes[1].children = [nodes[3], nodes[4]]
nodes[2].children = [nodes[1]]
nodes[3].children = [nodes[2], nodes[4]]

graph = Graph(nodes)
# graph.d
# ---")
graph.visited_nodes = {}
graph.bfs(nodes[0])
#print(nodes)
#print(graph.nodes[0].children[2])

