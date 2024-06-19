import collections

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    max_area = 0
    neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = set()
    
    def BFS(i,j):
        island = collections.deque()
        island.append( (i,j) )
        area = 0
        while island:
            area+=1
            land_i, land_j = island.pop()
            
            for i,j in neighbors:
                # if neighbor isnt in bound
                if not ( 0<=land_i+i<len(grid) and 0<=land_j+j<len(grid[0]) ):
                    continue

                # since neighbor is in bound
                if grid[land_i+i][land_j+j] == 1 and (land_i+i, land_j+j) not in seen:
                    island.append( (land_i+i, land_j+j) )
                    seen.add( (land_i+i, land_j+j) )
        return area
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i,j) not in seen:
                seen.add((i,j))
                max_area = max(max_area, BFS(i,j))

    return max_area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]


grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]


print(maxAreaOfIsland(grid))