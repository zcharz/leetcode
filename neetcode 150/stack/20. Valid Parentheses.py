class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {'}': '{', ']':'[', ')':'('}

        for c in s:
            if len(stack) and key.get(c, '') == stack[-1]:
                stack.pop()
                continue
            stack.append(c)

        return not len(stack)

sol = Solution ()
s = '()[]{}'
print(sol.isValid(s))