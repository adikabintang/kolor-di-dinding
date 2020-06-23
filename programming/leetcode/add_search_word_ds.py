# https://leetcode.com/problems/add-and-search-word-data-structure-design/
class TrieNode:
    def __init__(self, ch=None):
        self.ch = ch
        self.end = False
        self.children = [None] * 26
        self.n_children = 0
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        ptr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not ptr.children[idx]:
                ptr.children[idx] = TrieNode(c)
                ptr.n_children += 1
                
            ptr = ptr.children[idx]
        
        ptr.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.__helper(self.root, word)
    
    def __helper(self, root: TrieNode, word: str):
        ptr = root
        if not root:
            return False
        
        if len(word) == 0:
            return ptr.end
        b = False
        if word[0] == ".":
            for child in ptr.children:
                b = b or self.__helper(child, word[1:])
        else:
            idx = ord(word[0]) - ord('a')
            if not ptr.children[idx]:
                return False
            
            b = self.__helper(ptr.children[idx], word[1:])
        return b
        
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("cad")
assert obj.search("bad") == True
assert obj.search("cad") == True
assert obj.search("dad") == False
assert obj.search(".ad") == True
