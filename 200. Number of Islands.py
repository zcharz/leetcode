
# idea: iterate through each index
# with 2 for loops, O(M*N)
# when reaching a '1', perform BFS on that
# each time adding the visited values


def numIslands(grid: list[list[str]]) -> int:    
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def BFS(i,j):
        queue = [(i,j)]

        while queue:
            curr = queue.pop()
            i,j = curr[0], curr[1]
            visited.add((i,j))
            
            # add all neighbors thats not in visited and not out of bounds
            if grid[i][j] == '1':
                if (not i==0) and ((i-1,j) not in visited):
                    queue.append((i-1,j))
                if (not i==rows-1) and ((i+1,j) not in visited):
                    queue.append((i+1,j))
                if (not j==0) and ((i,j-1) not in visited):
                    queue.append((i,j-1))
                if (not j==cols-1) and ((i,j+1) not in visited):
                    queue.append((i,j+1))


    # neetcode BFS
    # import collections
    # def bfs(r,c):
        # q = collections.deque()
        # visited.add((r,c))
        # q.append((r,c))
    
        # while q:
        #     row,col = q.popleft()
        #     directions= [[1,0],[-1,0],[0,1],[0,-1]]
        
        #     for dr,dc in directions:
        #         r,c = row + dr, col + dc
        #         if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                
        #             q.append((r , c ))
        #             visited.add((r, c ))

    for i in range(rows):
        for j in range(cols):
            # if (i,j) in visited:
            #     continue

            if grid[i][j] == '1' and (i, j) not in visited:
                islands+=1
                BFS(i,j)

    return islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# grid = [["1","1","1"],["0","1","0"],["1","1","1"]]



print(numIslands(grid))