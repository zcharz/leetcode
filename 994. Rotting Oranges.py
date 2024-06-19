import collections

def orangesRotting(grid: list[list[int]]) -> int:
    c = 0

    # find all rotten oranges
    # OR edge case where there are no fresh oranges
    fresh = 0
    queue = collections.deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i,j))
            if grid[i][j] == 1:
                fresh+=1

    neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = set()

    # BFS to convert all fresh oranges to non fresh
    while queue and fresh>0:
        c+=1
        for i in range(len(queue)):
            rotten = queue.popleft()
            visited.add(rotten)

            for (n,m) in neighbors:
                x, y = rotten[0]+n, rotten[1]+m
                
                # new fresh oranges
                if (x,y) not in visited and 0<=x<len(grid) and 0<=y<len(grid[0]):
                    if grid[x][y]==1:
                        grid[x][y]=2
                        fresh-=1
                        queue.append( (rotten[0]+n,rotten[1]+m) )

    return c if fresh == 0 else -1



grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[0,2]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))