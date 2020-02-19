# https://www.python-course.eu/graphs_python.php
# http://www.openbookproject.net/books/pythonds/

from typing import Tuple

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        
        self.__graph_dict = graph_dict
    
    # vertices = nodes
    def vertices(self):
        return list(self.__graph_dict.keys())
    
    def edges(self):
        return self.__generate_edges()
    
    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def add_edge(self, edge: Tuple[str, str]):
        (vertex1, vertex2) = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def __generate_edges(self):
        edges = []
        for key, value in self.__graph_dict.items():
            for child in value:
                if {key, child} not in edges:
                    edges.append({key, child})

        return edges
    
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def find_path(self, src, dest, path=[]):
        if len(path) == 0:
            path = [src]
        else:
            path.append(src)
        if src == dest:
            return path
        
        children = self.__graph_dict[src]
        for child in children:
            if child not in path:
                x = self.find_path(child, dest, path)
                if dest in x:
                    return x
                # return x
        
        path.pop()
        return path

if __name__ == "__main__":
    g = { "a" : ["d", "g"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : [],
          "g" : ["a"]
        }
    
    graph = Graph(g)
    print("vertices graph:")
    print(graph.vertices())
    print(graph)
    print(graph.find_path("a", "d"))
    
    print(graph.find_path("c", "g"))
    print(graph.find_path("c", "e"))
    print(graph.find_path("a", "c"))
    print(graph.find_path("a", "f"))

# def find_isolated_nodes(graph):
#     isolated = []
#     for key in graph:
#         if len(graph[key]) == 0 or not graph[key]:
#             isolated.append(key)

#     return isolated

# print(generate_edges(graph))
