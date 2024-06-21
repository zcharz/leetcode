def solveNQueens(n: int) -> list[list[str]]:
    sols = []
    stack = []

    def backtrack(c):
        if c == n:
            sols.append(stack.copy())
            return 
    
        curr = ''
        for i in range(n):
            val = True
            for ind, queen in enumerate(stack):
                pos = queen.index('Q')

                if i==pos or i+c==pos+ind or i-c==pos-ind:
                    val=False
                    break

            if val:
                stack.append(f"{'.'*i}Q{'.'*(n-i-1)}")
                backtrack(c+1)
                stack.pop()
    
    backtrack(0)
    return sols



n = 4
print(solveNQueens(n))