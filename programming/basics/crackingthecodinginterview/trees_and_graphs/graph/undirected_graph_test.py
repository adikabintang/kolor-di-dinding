import unittest
from undirected_graph import Graph

class TestGraphMehods(unittest.TestCase):

    def test_find_path(self):
        g = { "a" : ["d", "g"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : [],
          "g" : ["a"]
        }
    
        graph = Graph(g)
        self.assertEqual(graph.find_path("a", "f"), [])
        self.assertEqual(graph.find_path("a", "g"), ["a", "g"])
        self.assertEqual(graph.find_path("a", "d"), ["a", "d"])
        self.assertEqual(graph.find_path("a", "c"), ["a", "d", "c"])
        self.assertEqual(graph.find_path("d", "e"), ["d", "c", "e"])
        self.assertEqual(graph.find_path("c", "g"), ["c", "d", "a", "g"])
        self.assertEqual(graph.find_path("e", "b"), ["e", "c", "b"])

if __name__ == "__main__":
    unittest.main()