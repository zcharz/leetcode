import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
            adjacency_list = {i+1:[] for i in range(n)}
            for u, v, w in times: adjacency_list[u].append((v,w))

            minheap = [(0, k)]
            dist = {vertex:float('inf') for vertex in adjacency_list}
            dist[k] = 0

            while minheap:
                curr_dist, curr_vertex = heapq.heappop(minheap)
                for next_vertex, weight in adjacency_list[curr_vertex]:
                    if dist[next_vertex] > curr_dist + weight:
                        dist[next_vertex] = curr_dist + weight
                        heapq.heappush(minheap, (dist[next_vertex], next_vertex))

            currmax = 0
            for delay in dist.values():
                if delay == float('inf'): return -1
                currmax = max(currmax, delay)
            return currmax
    
    
sol = Solution()

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(sol.networkDelayTime(times, n, k))

times = [[1,2,1]]
n = 2
k = 1
print(sol.networkDelayTime(times, n, k))