class Node:
    def __init__(self):
        self.next = dict()
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.start = Node()

    def addWord(self, word: str) -> None:
        curr = self.start
        for s in word:
            if s not in curr.next:
                curr.next[s] = Node()
            curr = curr.next[s]
        curr.isWord = True

    def search(self, word: str) -> bool:
        stack = [(self.start, 0)]
        while stack:
            curr, i = stack.pop()
            if i == len(word) and curr.isWord: return True
            elif i == len(word): continue

            if word[i] == '.':
                stack.extend([(curr.next[c], i+1) for c in curr.next])
            elif word[i] in curr.next:
                stack.append((curr.next[word[i]], i+1))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))