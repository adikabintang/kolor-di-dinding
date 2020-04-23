# https://www.geeksforgeeks.org/trie-insert-and-search/
# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
class TrieNode:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = []
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_a_word(self, word: str):
        ptr = self.root
        for ch in word:
            found = False
            # instead of linear search for looking up the children, 
            # we can use a hashtable for the children
            for child in ptr.children:
                if ch == child.ch:
                    ptr = child
                    found = True
                    break
            
            if not found:
                ptr.children.append(TrieNode(ch))
                ptr = ptr.children[-1]
        
        ptr.is_end_of_word = True
    
    def is_prefix_exist(self, prefix):
        ptr = self.root
        for c in prefix:
            found = False
            for child in ptr.children:
                if c == child.ch:
                    found = True
                    ptr = child
                    break
            
            if not found:
                return False
        
        return True
    
    def get_all_str_with_prefix(self, prefix):
        ptr = self.root
        s = ""
        arr = []
        for c in prefix:
            found = False
            for child in ptr.children:
                if c == child.ch:
                    s += c
                    found = True
                    ptr = child
                    break
            if not found:
                return arr
        s = s[:-1]
        arr = self.get_all_below_str_dfs(ptr)
        for i in range(len(arr)):
            arr[i] = s + arr[i]
        return arr
        
    def get_all_below_str_dfs(self, root: TrieNode, s=None, arr=None):
        if s is None:
            s = ""
        if arr is None:
            arr = []

        if root:
            s += root.ch
            if root.is_end_of_word:
                return [s]

            for child in root.children:
                arr.extend(self.get_all_below_str_dfs(child, s))
            
        return arr

t = Trie()
t.add_a_word("abde")
t.add_a_word("abdf")
t.add_a_word("abg")
t.add_a_word("az")
# print(t.is_prefix_exist("ab"))
# print(t.is_prefix_exist("bc"))
# print(t.is_prefix_exist("ac"))
print(t.get_all_str_with_prefix("ab"))