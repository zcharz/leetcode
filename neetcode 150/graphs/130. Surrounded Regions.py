class Solution:
    def solve(self, board: list[list[str]]) -> None:
        row, col = len(board), len(board[0])
        def dfs(i,j):
            stack = [(i,j)]
            while stack:
                i, j = stack.pop()
                if -1<i<row and -1<j<col and board[i][j] == 'O':
                    board[i][j] = 'T'
                    stack.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

        # iterating through top and bottom edge
        for i in range(col):
            if board[0][i] == 'O': 
                dfs(0,i)
            if board[row-1][i] == 'O':
                dfs(row-1, i)

        # iterating through left and right edge
        for i in range(row):
            if board[i][0] == 'O': 
                dfs(i, 0)
            if board[i][col-1] == 'O':
                dfs(i, col-1)

        # replace Os, which will be captured, by X
        # replcae T, which are safe, by O
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

                    

sol = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
print(board)

board = [["X"]]
sol.solve(board)
print(board)