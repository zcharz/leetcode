def exist(board: list[list[str]], word: str) -> bool:
    neighbors = [ (0,1), (0,-1), (1,0), (-1,0) ]
    rows = len(board)
    cols = len(board[0])
    seen = set()

    def dfs(i,j, length):
        # print(f' {board[i][j]} at {i},{j}  ind:{ind} word@ind:{word[ind]}  {seen}')
        if length == len(word):
            return True

        seen.add( (i,j) )
        for neigh_i, neigh_j in neighbors:
            x, y = i+neigh_i, j+neigh_j

            # if in bound, matches next letter, not seen yet
            if  0<=x<rows and 0<=y<cols and board[x][y] == word[length] and (x,y) not in seen:
                if dfs(x,y, length+1):
                    return True 
        seen.remove( (i,j) )
        return False

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                if dfs(i,j, 1):
                    return True
    
    return False


# neetcode solution
# same logic, un-nested some conditions
# has letter checking and boundary checking at the start rather than in iteration
# returns an or statement of all neighbors rather than using iteration


board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"


print(exist(board, word))