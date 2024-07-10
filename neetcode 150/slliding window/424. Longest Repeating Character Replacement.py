# shift right until all non-max characters total = k
# when total non-max > k: shift left until non-max = k again

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = [0 for i in range(26)]
        length = 1

        # simulating r
        for i in range(len(s)):
            count[ord(s[i])-65]+=1
            while sum(count) - max(count) > k: 
                count[ord(s[l])-65]-=1
                l+=1
            length = max(length, i-l+1)

        return length
    

sol = Solution()

s = "ABAB"
k = 2
print(sol.characterReplacement(s, k))

s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))

s = "ABAA"
k = 0
print(sol.characterReplacement(s, k))