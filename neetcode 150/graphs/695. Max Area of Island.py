class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        size = 0

        def dfs(i,j):
            count = 0
            stack = [(i,j)]
            while stack:
                i, j = stack.pop()
                if (i,j) in seen: continue

                if (i,j) not in seen:
                    seen.add((i,j))
                    count+=1

                for x, y in dir:
                    r, c = i+x, j+y
                    if -1<r<rows and -1<c<cols and grid[r][c] and (r,c) not in seen:
                        stack.append((r,c))
                        
            return count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (i,j) not in seen:
                    size = max(size, dfs(i,j))

        return size


sol = Solution()

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(sol.maxAreaOfIsland(grid))

# grid = [[0,0,0,0,0,0,0,0]]
# print(sol.maxAreaOfIsland(grid))

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]]
print(sol.maxAreaOfIsland(grid))