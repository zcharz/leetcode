class Node:
    def __init__(self):
        self.isword = False
        self.next = dict()


class WordDictionary:

    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        curr =  self.trie
        for i in word:
            if i not in curr.next:
                curr.next[i] = Node()
            curr = curr.next[i]
        curr.isword = True

    def search(self, word: str) -> bool:
        curr = self.trie

        def helper(node, ind):
            if ind == len(word) and node.isword:
                return True
            elif ind==len(word):
                return False

            if word[ind] == '.':
                for i in node.next:
                    if helper(node.next[i], ind+1):
                        return True
            elif word[ind] in node.next:
                return helper(node.next[word[ind]], ind+1)
            return False

        return helper(curr, 0)