class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        pass

sol = Solution()

board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(sol.findWords(board, words))

board = [["a","b"],
         ["c","d"]]
words = ["abcb"]
print(sol.findWords(board, words))