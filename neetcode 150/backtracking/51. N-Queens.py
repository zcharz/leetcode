class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res, stack = [], []
        seencol, dialeft, diaright = set(), set(), set()

        def backtrack(row):
            if row == n:
                board = [''.join(['Q' if i == piece else '.' for i in range(n)]) for piece in stack]
                res.append(board)
                return

            for col in range(n):
                diar = row - col
                dial = row + col

                if col in seencol or diar in diaright or dial in dialeft:
                    continue
                stack.append(col)
                seencol.add(col)
                dialeft.add(dial)
                diaright.add(diar)

                backtrack(row+1)

                seencol.remove(col)
                dialeft.remove(dial)
                diaright.remove(diar)
                stack.pop()

        backtrack(0)
        return res


sol = Solution()
boards = sol.solveNQueens(4)

for b in boards:
    for row in b:
        print(row)
    print()

boards = sol.solveNQueens(1)

for b in boards:
    for row in b:
        print(row)
    print()



# row - col
# 0 -1 -2 -3
# 1 0 -1 -2
# 2 1 0 1
# 3 2 1 0

# col + row
# 0 1 2 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6