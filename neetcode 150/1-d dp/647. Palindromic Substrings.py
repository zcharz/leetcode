class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        for start in range(len(s)):
            # odd palindromes
            ret += self.counter(s, start, start)
            # even palindromes
            ret += self.counter(s, start, start+1)
        return ret
    
    def counter(self, s, l, r):
        ret = 0
        while l>-1 and r<len(s) and s[l] == s[r]:
            ret+=1
            l-=1
            r+=1
        return ret


sol = Solution()
s = "abc"
print(sol.countSubstrings(s))