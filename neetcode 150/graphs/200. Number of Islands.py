import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        seen = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen or grid[i][j]=='0': continue

                queue = collections.deque()
                queue.append((i,j))

                while queue:
                    x, y = queue.popleft()
                    if x<0 or x>len(grid)-1 or y<0 or y>len(grid[0])-1 or grid[x][y] == '0' or (x,y) in seen: continue
                    seen.add((x,y))
                    queue.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
                count+=1

        return count


sol = Solution()
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# print(sol.numIslands(grid))

grid = [["1","0"]]
print(sol.numIslands(grid))