class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ret = []
        stack = []

        def dfs(open, close):
            if close == n:
                ret.append(''.join(stack))
                return

            if open<n:
                stack.append('(')
                dfs(open+1, close)
                stack.pop()

            if close<open:
                stack.append(')')
                dfs(open, close+1)
                stack.pop()

        dfs(0, 0)
        return ret


sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))