# minimum spanning tree
# each point, a theoretical connection to all other nodes exist
# create all theoretical connections O(n*n)
# sort by length O(n^2logn^2)
# union find to check for cycles, 
# adding only min edges that don't create a cycle 
# until all nodes are connected

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        points = [tuple(p) for p in points]
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((points[i], points[j]))
        edges.sort(key = lambda edge: abs(edge[0][0]- edge[1][0]) + abs(edge[0][1] - edge[1][1]))

        parent = {p:p for p in points}
        rank = {p:0 for p in points}

        def find(n):
            if parent[n] == n: return n
            else:
                parent[n] = find(parent[n])
                return parent[n]
            
        def union(a, b):
            a, b = find(a), find(b)
            if a==b: return True
            if rank[a] > rank[b]: parent[b] = a
            elif rank[a] < rank[b]: parent[a] = b
            else:
                rank[a]+=1
                parent[b] = a
            return False
        
        edgecount = 0
        mincost = 0
        for edge in edges:
            if edgecount == len(points)-1: return mincost
            if union(edge[0], edge[1]): continue
            edgecount+=1
            mincost += abs(edge[0][0]- edge[1][0]) + abs(edge[0][1] - edge[1][1])
        return 0


sol = Solution()

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(sol.minCostConnectPoints(points))

points = [[3,12],[-2,5],[-4,1]]
print(sol.minCostConnectPoints(points))