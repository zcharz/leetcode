class Node:
    def __init__(self):
        self.word = False
        self.next = dict()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.next:
                node.next[s] = Node()
            node = node.next[s]
        node.word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for s in word:
            if s not in node.next:
                return False
            node = node.next[s]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for s in prefix:
            if s not in node.next:
                return False
            node = node.next[s]

        # implicity that if this node exists, 
        # there must be children that starts with the prefix
        # or this prefix is a word
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

sol = Trie()
sol.insert('apple')

# sol.insert('a')
print(sol.root.next)




# print(sol.startsWith('a'))
# sol.insert('a')