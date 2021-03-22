



class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.endHere = False

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.endHere = True

trie = Trie()
trie.insert("help")

print(trie)







Trie trie = Trie