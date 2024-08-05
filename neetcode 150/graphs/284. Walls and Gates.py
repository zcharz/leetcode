# premium problem
# solving neetcode version

# initial idea: BFS from all points, replace value with first layer it finds treasure
# second idea: reverse thinking from previous, BFS from all treasure, where
#   if the value currently is INF, replace with current layer
#   if the value is currently less than current layer, stop here
#   if value is greater, continue to BFS on its neighbors

from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        treasure = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0: treasure.append((0,i,j))

        while treasure: 
            dist, i, j = treasure.popleft()
            if grid[i][j] == -1 or grid[i][j] < dist: continue
            grid[i][j] = dist

            for x,y in directions:
                r, c = i+x, j+y
                if -1<r<ROWS and -1<c<COLS:
                    treasure.append((dist+1, r,c))
            


sol = Solution()
grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
for row in grid:
    print(row)
sol.islandsAndTreasure(grid)
for row in grid:
    print(row)