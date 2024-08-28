# reverse thinking
# from pacific side, bfs/dfs to find all elements which reaches pacific
# from atlantic side, find all elements which reaches atlantic

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i,j, seen):
            stack = [(i,j)]
            while stack: 
                currx, curry = stack.pop()
                if (currx, curry) in seen: continue
                seen.add((currx, curry))

                for x, y in dir:
                    i, j = currx+x, curry+y
                    if -1<i<ROW and -1<j<COL and heights[i][j]>=heights[currx][curry]:
                        stack.append((i,j))

        # first element in each row (first col) for pacific
        # last element in each row (last col) for atlantic
        for i in range(ROW):
            dfs(i, 0, pacific)
            dfs(i, COL-1, atlantic)

        # all elements in first row for pacific
        # all elements in last row for atlantic
        for i in range(COL):
            dfs(0, i, pacific)
            dfs(ROW-1, i, atlantic)

        return list(pacific.intersection(atlantic))


sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))

heights = [[1,1],[1,1],[1,1]]
print(sol.pacificAtlantic(heights))