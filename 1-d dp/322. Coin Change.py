
# O(n^2) solution
# TLE
def coinChange(coins: list[int], amount: int) -> int:
    dp = [-1 for i in range(amount+1)]
    for c in coins:
        if c<=amount:
            dp[c] = 1
    dp[0] = 0
    # index = current amount

    for i in range(amount+1):
        for j in range(1, i//2+1):
            # print(f'{i} start={j}  end={i-j}')
            # skip when combination is invalid
            if not (dp[j]!=-1 and dp[i-j] != -1):
                continue
            # fill with first available value
            if dp[i] == -1:
                dp[i] = dp[j] + dp[i-j]
            # replace with lower value when applicable
            else:
                dp[i] = min(dp[i], dp[j] + dp[i-j])

    return dp[-1]


# "steps" solution
# for each coin, see if dp[amount-coinval] + 1 < dp[amount]
# keep min value at each amount 
# O(n*m) time, n = amount, m = # of coins
# O(n) space with 1d array
def coinChange(coins: list[int], amount: int) -> int:
    dp = [-1 for i in range(amount+1)]
    dp[0] = 0
    for c in coins:
        for i in range(c, amount+1):
            # if the previous value doesn't exist, skip
            if dp[i-c]==-1:
                continue
            # if the previuos value exists
            # and current value is placeholder, replace it
            if dp[i]==-1:
                dp[i] = dp[i-c] + 1
            # take the min between current value and new value
            else:
                dp[i] = min(dp[i], dp[i-c]+1)
    
    # print(dp)
    return dp[-1]


coins = [1,2,5]
amount = 11

print(coinChange(coins, amount))