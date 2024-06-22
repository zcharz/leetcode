class Solution:
    def isPalindrome(self, s: str) -> bool:
        # in place solution -> O(2n) time
        s = [c for c in s.lower() if c.isalnum()]
        s = ''.join(s)
        l, r = 0, len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return False
            l, r = l+1, r-1
        return True

        # return s == s[::-1]
    
sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))