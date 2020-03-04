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
                xtended_path = self.find_path(child, dest, path)
                if dest in xtended_path:
                    return xtended_path
        
        path.pop()
        return path
    
    # THIS IS BAD, SO BAD
    # [] as default argument in python is discourage, see this:
    # https://stackoverflow.com/questions/366422/what-is-the-pythonic-way-to-avoid-default-parameters-that-are-empty-lists
    def find_all_paths(self, src, dst, path=[]):
        path = path + [src]
        
        if src == dst:
            return [path]
        if src not in self.__graph_dict:
            return []
        
        all_paths = []
        for v in self.__graph_dict[src]:
            if v not in path:
                extended_path = self.find_all_paths(v, dst, path)
            
                for p in extended_path:
                    all_paths.append(p)
            
        return all_paths

    def vertex_degree(self, vertex):
        children = self.__graph_dict[vertex]
        count = len(children) + children.count(vertex)        
        return count
    
    def find_isolated_vertices(self):
        isolated = []
        for vertex, children in self.__graph_dict.items():
            if len(children) == 0:
                isolated.append(vertex)
            
        return isolated
    
    def min_degree(self):
        flag = False
        min_d = 0
        for v in self.__graph_dict:
            m = self.vertex_degree(v)
            if flag == False:
                min_d = m
                flag = True
            if m < min_d:
                min_d = m
        
        return min_d
    
    def max_degree(self):
        max_d = 0
        for v in self.__graph_dict:
            m = self.vertex_degree(v)
            if m > max_d:
                max_d = m
        return max_d
    
    def is_connected(self):
        all_vertices = list(self.__graph_dict.keys())
        point = all_vertices[0] if len(all_vertices) > 0 else None

        for v in all_vertices:
            if len(self.find_path(point, v)) == 0:
                return False
        
        return True
    
    def diameter(self):
        diam = -1
        all_vertices = list(self.__graph_dict.keys())
        for i in range(0, len(all_vertices)):
            v1 = all_vertices[i]
            for j in range(i+1, len(all_vertices)):
                v2 = all_vertices[j]
                all_paths = self.find_all_paths(v1, v2)
                shortest_path = -1
                for path in all_paths:
                    path_distance = len(path) - 1
                    if shortest_path == -1:
                        shortest_path = path_distance
                    
                    if path_distance < shortest_path:
                        shortest_path = path_distance
                
                if diam == -1:
                    diam = shortest_path
                
                if shortest_path > diam:
                    diam = shortest_path
        
        return diam

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
