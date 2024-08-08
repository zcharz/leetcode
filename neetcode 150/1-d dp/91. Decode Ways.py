class Solution:
    def numDecodings(self, s: str) -> int:
        p1, p2 = 0, 1

        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                continue
            p2 = p2 + p1 + 1

            # print(p2, p1)
        return p2


sol = Solution()

# s = "12"
# print(sol.numDecodings(s))

s = "226"
print(sol.numDecodings(s))

s = "06"
print(sol.numDecodings(s))