# Premium question, solved on Neetcode.IO

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) >= n: return False
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2): return False

        for i in range(n):
            find(i)
            if i != 0:
                if par[i]!=par[i-1]: return False
        return True



sol = Solution()

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(sol.validTree(n, edges))

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(sol.validTree(n, edges))