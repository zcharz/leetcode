class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for word in wordDict:
                end = i+len(word)
                if end<=len(s) and s[i:end] == word and dp[i]:
                    dp[end] = True
        return dp[-1]
    

sol = Solution()

s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(sol.wordBreak(s, wordDict))

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
print(sol.wordBreak(s, wordDict))