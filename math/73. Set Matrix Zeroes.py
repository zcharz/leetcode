# O(m+n) space
# O(mn) time -> best theoretical time complexity
def setZeroes(matrix: list[list[int]]) -> None:
    row, col = len(matrix), len(matrix[0])
    changes = {'rows': set(), 'cols': set()}
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                changes['rows'].add(i)
                changes['cols'].add(j)
    
    for r in changes['rows']:
        for i in range(col):
            matrix[r][i] = 0
    for c in changes['cols']:
        for i in range(row):
            print(i)
            matrix[i][c] = 0


# O(1) space solution
def setZeroes(matrix: list[list[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]

setZeroes(matrix)
print(matrix)
