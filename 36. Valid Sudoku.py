def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if board[i][j] == '.':
                continue

            if board[i][j] in row:
                print(f'row {i}, index {j}')
                return False
            row.add(board[i][j])

            if board[j][i] in col:
                print(f'col {i}, index {j}')
                return False
            
            if board[j][i] != '.':
                col.add(board[j][i])

    for i in range(3):
        for j in range(3):
            box = set()
            row = i*3
            col = j*3

            for n in range(9):
                if board[row][col] == '.':
                    continue

                box.add(board[row][col])

                if board[row][col] in box:
                    print(f'box {i} {j}')
                    return False

                if (n+1)%3 == 0 and n!=0:
                    row+=1
                    col=j*3
                    continue
                col+=1
    return True



board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

test = [
["A","3",".","B","7",".","C",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["D",".",".","E","6",".","G",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,["G","6",".","H",".",".","I","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))


