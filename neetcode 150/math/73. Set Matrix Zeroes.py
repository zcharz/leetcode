# using first column to store if row need to be swapped
# using first row to store if col needs to be swapped

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        col0 , row0 = False, False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    if i == 0: row0 = True
                    else: matrix[0][j] = 0 
                    if j == 0: col0 = True
                    else: matrix[i][0] = 0

        # swap cols by looking at first of each col (first row)
        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(ROWS):
                    matrix[r][c] = 0

        # swap rows by looking at first of each row (first col)
        for r in range(1,ROWS):
            if matrix[r][0] == 0:
                for c in range(COLS):
                    matrix[r][c] = 0

        # swap col0 if it needs to be swapped
        if col0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # swap row0 if it needs to be swapped
        if row0:
            for c in range(COLS):
                matrix[0][c] = 0


sol = Solution()

# matrix = [
#     [1,1,1],
#     [1,0,1],
#     [1,1,1]]
# sol.setZeroes(matrix)
# for row in matrix:
#     print(row)

print()

matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]]
sol.setZeroes(matrix)
for row in matrix:
    print(row)

print() 

# matrix = [
#     [1,2,3,4],
#     [5,0,7,8],
#     [0,10,11,12],
#     [13,14,15,0]]
# sol.setZeroes(matrix)
# for row in matrix:
#     print(row)