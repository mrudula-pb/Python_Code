
class Trie:
    def __init__(self):
        self.root = {'*':'*'}

    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node['*'] = '*'

    def does_word_exist(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
                current_node = current_node
            current_node = current_node[letter]
        return '*' in current_node


trie = Trie()

words = {'wait'}

for word in words:
    trie.add_word(word)

print(trie.does_word_exist("wait"))
print(trie.does_word_exist(""))
print(trie.does_word_exist("waite"))
print(trie.does_word_exist("shop"))
print(trie.does_word_exist("shopppp"))