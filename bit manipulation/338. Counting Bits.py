
# O(n log n) solution
def countBits(n: int) -> list[int]:
    ans = []

    for i in range(n+1):
        # log n calculation
        c = 0

        while i!=0:
            c+=1
            i &= i - 1
            # bitwise and with itself -1
            # anding the number results in one less 1 bit
        ans.append(c)
    return ans

# O(n) dp solution
def countBits(n: int) -> list[int]:
    dp = [0]
    offset = 1

    for i in range(1,n+1):
        if i==offset*2:
            offset*=2
        # dp[i] = 
        dp.append(1+dp[i-offset])
    return dp

test = 5
print(countBits(test))