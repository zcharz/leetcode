class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n1, n2 = 0, 0
        for c in cost:
            n1, n2 = n2, min(n1+c, n2+c)
        return min(n1, n2)


sol = Solution()

cost = [10,15,20]
print(sol.minCostClimbingStairs(cost))

# cost = [1,100,1,1,1,100,1,1,100,1]
# print(sol.minCostClimbingStairs(cost))