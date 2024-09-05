# modified DFS with number of stops occured already
#   times out

# dijkstras from src, return distance[dst]

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        flights.sort(key=lambda x: x[2])
        adjlist = {i:[] for i in range(n)}
        for f in flights: adjlist[f[0]].append((f[1],f[2]))
        seen = set()

        def dfs(curr, currcost, stops):
            if curr == dst: return currcost
            if stops > k: return -1

            seen.add(curr)
            for destination, cost in adjlist[curr]:
                if destination in seen: continue
                endcost = dfs(destination, currcost+cost, stops+1)
                if endcost != -1: return endcost
            seen.remove(curr)
            return -1

        return dfs(src, 0, 0)
    

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