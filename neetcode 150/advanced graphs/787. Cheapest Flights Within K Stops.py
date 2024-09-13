import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adjacency_list = {i:[] for i in range(n)}
        for f in flights: adjacency_list[f[0]].append((f[1],f[2]))

        minheap = [(0, 0, src)]
        dist = {vertex:float('inf') for vertex in adjacency_list}
        dist[src] = 0

        while minheap:
            curr_stops, curr_dist, curr_vertex = heapq.heappop(minheap)

            for next_vertex, weight in adjacency_list[curr_vertex]:
                if not dist[next_vertex] > curr_dist + weight: continue
                if next_vertex == dst and curr_stops <= k:
                    dist[next_vertex] = curr_dist + weight
                elif curr_stops < k:
                    dist[next_vertex] = curr_dist + weight
                    heapq.heappush(minheap, (curr_stops+1, dist[next_vertex], next_vertex))
        
        return dist[dst] if dist[dst] != float('inf') else -1
        
    

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