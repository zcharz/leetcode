class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curr = set()
        ret = 0

        while r<len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            r+=1
            ret = max(ret, len(curr))

        return ret

sol = Solution()

s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))

s = "bbbbb"
print(sol.lengthOfLongestSubstring(s))

s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))