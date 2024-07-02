import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {'*', '/', '+', '-'}

        for t in tokens: 
            if t not in operations:
                stack.append(int(t))
                continue
            first = stack.pop()
            second = stack.pop()
            # stack.append( int( eval( str(second)+t+str(first) ) ) )

            if t=='+': stack.append(first+second)
            elif t=='*': stack.append(first*second)
            elif t=='-': stack.append(second-first)
            else: stack.append(int(second/first))
            # int() always truncates to 0

        return stack[-1]


sol = Solution()


# tokens = ["2","1","+","3","*"]
# print(sol.evalRPN(tokens))

# tokens = ["4","13","5","/","+"]
# print(sol.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))