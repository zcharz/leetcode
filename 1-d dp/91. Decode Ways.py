def numDecodings(s: str) -> int:
    dp = [0 for i in range(len(s)+1)]
    dp[-1] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and (
            s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
        ):
            dp[i] += dp[i + 2]

    return dp[0]
    


a = '226' #3
b = '12' #2
c = '06' #0
d = '10' #1
e = '2101' #1

test = [a,b,c,d,e]

for s in test:
    print(numDecodings(s))