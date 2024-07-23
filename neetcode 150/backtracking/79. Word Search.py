class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row, col, = len(board), len(board[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()

        def dfs(i,j, ind):
            if ind == len(word): return True

            if (i,j) in seen: return False
            if i<0 or i>row-1 or j<0 or j>col-1: return False
            if board[i][j] != word[ind]: return False

            # only add current to path if it exists and is the correct character
            seen.add((i,j))
            for x,y in dir:
                r,c = i+x, j+y
                if dfs(r, c, ind+1): return True
            seen.remove((i,j))
            return False

        for i in range(row):
            for j in range(col):
                if dfs(i,j, 0): return True
        return False


sol = Solution()


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(sol.exist(board, word))

board = [["a","b"],["c","d"]]
word = "acdb"
print(sol.exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(sol.exist(board, word))

board = [["a","a"]]
word = "aaa"
print(sol.exist(board, word))

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(sol.exist(board, word))