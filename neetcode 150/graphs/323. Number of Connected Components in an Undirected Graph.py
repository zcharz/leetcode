# Premium problem
# solved on neetcode.io

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        height = [0]*n

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(a, b):
            a, b = find(a), find(b)
            if a==b:

                return 0
            if height[a] > height[b]:
                parent[b] = a
            elif height[b] > height[a]:
                parent[a] = b
            else:
                height[a]+=1
                parent[b] = a
            return 1
        
        ret = 0
        for a, b in edges:
            ret+=union(a,b)
        return n-ret
        

sol = Solution()

n = 3
edges = [[0,1], [0,2]]
print(sol.countComponents(n, edges))

n = 6
edges = [[0,1], [1,2], [2,3], [4,5]]
print(sol.countComponents(n, edges))

n = 6
edges=[[0,1],[2,3],[4,5],[1,2],[3,4]]
print(sol.countComponents(n, edges))