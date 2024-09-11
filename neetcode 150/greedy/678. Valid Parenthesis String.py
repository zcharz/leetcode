class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, count = [], []
        for i, c in enumerate(s):
            if c == '(': stack.append( (c, i) )
            elif c=='*': count.append(i)
            else:
                if stack and stack[-1][0] == '(': stack.pop()
                elif count: count.pop()
                else: return False

        while stack:
            if not count: return False
            if stack[-1][1] < count[-1]:
                stack.pop()
                count.pop()
            else: return False
        return True


sol = Solution()

# s = "()"
# print(sol.checkValidString(s))

# s = "(*)"
# print(sol.checkValidString(s))

# s = "(*))"
# print(sol.checkValidString(s))

s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(sol.checkValidString(s))