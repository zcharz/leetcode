import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = collections.deque()
        seen = set()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j]==1: 
                    fresh+=1

        # edge case: no oranges at all
        if not fresh: return 0

        count = -2
        while queue: 
            for n in range(len(queue)):
                i,j = queue.popleft()
                if (i,j) in seen or i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j] == 0: continue
                if grid[i][j] == 1: fresh-=1
                seen.add((i,j))
                queue.extend([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
            count+=1
        return count if not fresh else -1
    

sol = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid))

# grid = [[2,1,1],[0,1,1],[1,0,1]]
# print(sol.orangesRotting(grid))