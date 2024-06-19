def climbStairs(n: int) -> int:
    dp = [0 for i in range(n+1)]

    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[-1]


# O(1) space solution
# since each next number only depends on previous 2,
# only keep 2/3 numbers at a time, update per iteration
def climbStairs(n: int) -> int:
    if n <= 3:
        return n
    n1, n2 = 2, 3

    for i in range(4, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2