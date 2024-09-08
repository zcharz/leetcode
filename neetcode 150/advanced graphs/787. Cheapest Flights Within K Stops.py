# modified DFS with number of stops occured already
#   times out

# dijkstras from src, return distance[dst]

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adjlist = {i:[] for i in range(n)}
        for f in flights: adjlist[f[0]].append((f[1],f[2]))
      
        for i in len(adjlist):
    

sol = Solution()

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(sol.findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(sol.findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(sol.findCheapestPrice(n, flights, src, dst, k))