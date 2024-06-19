def minCostClimbingStairs(cost: list[int]) -> int:
    dp = []

    dp.append(0)
    dp.append(0)

    for i in range(2, len(cost)+1):

        print(min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]))
        dp.append( min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) )

    print(dp)

    return dp[-1]



test = [10,15,20]

print(minCostClimbingStairs(test))