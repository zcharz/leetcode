class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2*n1)
            elif t == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2+n1)
            elif t == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif t == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            else:
                stack.append(int(t))

        return stack[0]


sol = Solution()
tokens = ["2","1","+","3","*"]
print(sol.evalRPN(tokens))