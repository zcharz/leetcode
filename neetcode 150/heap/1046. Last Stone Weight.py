import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            s3 = s1 - s2
            if s3: heapq.heappush(stones, s3)

        return -stones[0] if stones else 0

sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))