import collections

# idea:
# O(M-2 * N-2) iteration through all elements in inner 
# skip elements that are seen
# if element is O, BFS over element 

# time complexity: O(MN)
# iteration through all elements O(MN)
# since elements are skipped if they are seen
# worst case replacing all Os to Xs besides border, O(MN)
# O(N) extra space -> seen set may take entire board

def solve(board: list[list[str]]) -> None:
    row, col = len(board), len(board[0])
    
    if row <3 or col<3:
        return

    seen = set()
    neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

    def BFS(i,j):
        queue = collections.deque()
        queue.append((i,j))
        this = set()
        flip = True
        
        while queue:
            curr = queue.pop()
            seen.add(curr)
            this.add(curr)

            for n,m in neighbors:
                x,y = curr[0]+n, curr[1]+m
                edge = False
                if 0==x or x==row-1 or 0==y or y==col-1:
                    edge = True

                # if neighbor is a border O
                # after finding all adjacent Os, flip 
                if board[x][y]=='O' and edge:
                    flip = False

                elif board[curr[0]+n][curr[1]+m]=='O' and (x,y) not in seen:
                    queue.append( (curr[0]+n, curr[1]+m) )

        if flip:
            for (n,m) in this:
                board[n][m] = 'X'

    for i in range(1, row-1):
        for j in range(1,col-1):
            if board[i][j] == 'O' and (i,j) not in seen:
                BFS(i,j)


test = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

solve(test)

for line in test:
    print(line)



# neetcode solution
# rather than change all regions surroudned
# change all regions except those connected to boarder
# 2 part algo:
# scan edge for Os, O(2M+2N)
# on those Os, find all connected Os and change them to T (temp)
# change all Os to Xs, O(NM)
# change all Ts back to Os, O(NM)
# in place changes, O(1) extra space