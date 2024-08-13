class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount: return 0

        dp = [0 for i in range(amount+1)]
        for c in coins:
            if c<=amount: dp[c] = 1

        for i in range(1, amount+1):
            if dp[i]: pass
            else:
                currmin = amount+1
                for c in coins:
                    if i-c>0 and dp[i-c]:
                        currmin = min(dp[i-c], currmin)
                if currmin != amount+1:
                    dp[i] = currmin+1

        return dp[amount] if dp[amount] else -1


sol = Solution()

coins = [1,2,5]
amount = 11
print(sol.coinChange(coins, amount))

coins = [2]
amount = 3
print(sol.coinChange(coins, amount))

coins = [1]
amount = 0
print(sol.coinChange(coins, amount))

coins = [3]
amount = 4
print(sol.coinChange(coins, amount))
