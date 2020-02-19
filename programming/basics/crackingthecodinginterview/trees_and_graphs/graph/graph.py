class Node:
    def __init__(self, name=None, children=[]):
        self.name = name
        self.children = children

    def __repr__(self):
        return str(str(self.name) + ": " + str(self.children))


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.visited_nodes = {}

    def dfs(self, a_node):
        if a_node:
            print(a_node.name)
            self.visited_nodes[a_node.name] = True
            for n in a_node.children:
                if self.visited_nodes.get(n.name) == None:
                    self.dfs(n)     
    
    def bfs(self, a_node):
        queue = []
        self.visited_nodes[a_node.name] = True
        queue.append(a_node)

        while queue:
            parent = queue.pop(0)
            print(parent.name)
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

