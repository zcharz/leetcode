# idea: 
# for each value bordering pacific, run WFS (whatever first search)
# to find all values that can reach this edge

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def dfs(input):
            stack = input
            seen = set()

            while stack:
                i, j = stack.pop()
                if (i,j) in seen: continue
                seen.add((i,j))

                for r, c in direction:
                    x, y = i+r, j+c
                    if -1<x<ROWS and -1<y<COLS and heights[i][j] <= heights[x][y]:
                        stack.append((x,y))
            return seen

        pacificstack, atlanticstack = [],[]
        for i in range(ROWS):
            pacificstack.append((i, 0))
            atlanticstack.append((i, COLS-1))
        for i in range(COLS):
            pacificstack.append((0, i))
            atlanticstack.append((ROWS-1, i))

        pacific = dfs(pacificstack)
        atlantic = dfs(atlanticstack)
        return list(pacific.intersection(atlantic))


sol = Solution()
# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# print(sol.pacificAtlantic(heights))

heights = [[1,1],[1,1],[1,1]]
print(sol.pacificAtlantic(heights))