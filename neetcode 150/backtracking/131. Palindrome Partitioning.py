class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ret, stack = [], []

        def dfs(ind):
            if ind == len(s):
                ret.append(stack.copy())
                return

            for i in range(ind, len(s)):
                currstr = s[ind:i+1]
                if currstr == currstr[::-1]:
                    stack.append(currstr)
                    dfs(i+1)
                    stack.pop()

        dfs(0)
        return ret


sol = Solution()

s = 'aab'
print(sol.partition(s))

s = 'a'
print(sol.partition(s))