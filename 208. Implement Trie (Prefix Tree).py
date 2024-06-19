class Node:
    def __init__(self):
        self.isword = False
        self.next = dict()

class Trie:
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.next:
                node.next[c] = Node()
            node = node.next[c]
        node.isword = True


    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]
        return node.isword


    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c not in node.next:
                return False
            node = node.next[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)