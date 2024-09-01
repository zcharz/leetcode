class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0': return 0

        dp = [0 for i in range(len(s)+1)]
        if s[len(s)-1] != '0': dp[len(s)-1] = 1
        dp[len(s)] = 1

        for i in range(len(s)-2, -1, -1):
            if s[i] == '0': continue

            curr = dp[i+1]            

            if 9<int(s[i:i+2])<27: curr+=dp[i+2]
            dp[i] = curr

        # print(dp)
        return dp[0]


sol = Solution()

s = "12"
print(sol.numDecodings(s))

s = "226"
print(sol.numDecodings(s))

s = "06"
print(sol.numDecodings(s))