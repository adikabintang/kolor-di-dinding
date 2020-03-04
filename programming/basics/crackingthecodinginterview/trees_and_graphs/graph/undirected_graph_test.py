import unittest
from undirected_graph import Graph


class TestGraphMehods(unittest.TestCase):
    def setUp(self):
        self.graph = Graph({"a": ["d", "g"],
                            "b": ["c"],
                            "c": ["b", "c", "d", "e"],
                            "d": ["a", "c"],
                            "e": ["c"],
                            "f": [],
                            "g": ["a"]
                            })
        self.another_graph = Graph({
            "a": ["c"],
            "b": ["c", "e", "f"],
            "c": ["d", "e"],
            "d": ["c"],
            "e": ["b", "c", "f"],
            "f": ["b", "e"]
        })

    def test_find_path(self):
        self.assertEqual(self.graph.find_path("a", "f"), [])
        self.assertEqual(self.graph.find_path("a", "g"), ["a", "g"])
        self.assertEqual(self.graph.find_path("a", "d"), ["a", "d"])
        self.assertEqual(self.graph.find_path("a", "c"), ["a", "d", "c"])
        self.assertEqual(self.graph.find_path("d", "e"), ["d", "c", "e"])
        self.assertEqual(self.graph.find_path("c", "g"), ["c", "d", "a", "g"])
        self.assertEqual(self.graph.find_path("e", "b"), ["e", "c", "b"])

    def test_vertex_degree(self):
        self.assertEqual(self.graph.vertex_degree("a"), 2)
        self.assertEqual(self.graph.vertex_degree("c"), 5)
        self.assertEqual(self.graph.vertex_degree("f"), 0)

    def test_is_connected(self):
        self.assertEqual(self.graph.is_connected(), False)
        self.assertEqual(self.another_graph.is_connected(), True)

    def test_diameter(self):
        self.assertEqual(self.another_graph.diameter(), 3)


if __name__ == "__main__":
    unittest.main()
