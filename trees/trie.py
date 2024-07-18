"""
Tries
- general binary tree
- root node is empty
- children is a dictionary - easier to navigate than using an array
- usecase : auto completes
"""
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True
    
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end == True
        
    def remove(self, word):
        """
        Its always the remove case that makes my brain fry

        1. word to be removed is a prefix : last ch has children, remove end property of last ch
        2. contains prefix to other words eg. heart could have he prefixing her and hea prefixing head
            - in this case remove everything except the ones prefixing 
            - if len of children is just one on that path pop and return

        Current implementation keeps the words but remove the end property. More space but saves some computation
        """
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return
            curr = curr.children[ch]
        curr.end = False
"""
TESTING
"""

t = Trie()

t.insert("pies")
t.insert("pied")

print("search for pie -false: ", t.search("pie"))
print("search for pies - true: ", t.search("pies"))
print("search for pied - true: ", t.search("pied"))
print("search for pi - false: ", t.search("pi"))

t.insert("pi")

print("search for pi after insertion - true: ", t.search("pi"))

t.remove("pi")

print("search for pi after deletion - False: ", t.search("pi"))

print("search for pie -false: ", t.search("pie"))
print("search for pies - true: ", t.search("pies"))
print("search for pied - true: ", t.search("pied"))