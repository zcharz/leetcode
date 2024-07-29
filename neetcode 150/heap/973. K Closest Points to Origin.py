import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        ret = []
        points = [(i*i + j*j, i, j) for i,j in points]
        heapq.heapify(points)
        for i in range(k):
            dist, i, j = heapq.heappop(points)
            ret.append([i,j])
        return ret

sol = Solution()

points = [[1,3],[-2,2]]
k = 1
print(sol.kClosest(points, k))