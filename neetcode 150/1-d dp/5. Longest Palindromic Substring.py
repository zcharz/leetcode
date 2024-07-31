class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstr = ''

        for start in range(len(s)):
            l, r = start, start
            while l>-1 and r<len(s) and s[l] == s[r]:
                if r-l+1 > len(maxstr): maxstr = s[l:r+1]
                l-=1
                r+=1
            
            l, r = start, start+1
            while l>-1 and r<len(s) and s[l] == s[r]:
                if r-l+1 > len(maxstr): maxstr = s[l:r+1]
                l-=1
                r+=1

        return maxstr


sol = Solution()

s = "babad"
print(sol.longestPalindrome(s))