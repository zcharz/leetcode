class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        pass

sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(sol.ladderLength(beginWord, endWord, wordList))