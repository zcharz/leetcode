
# recursive O(3^N) solution
# sinice each recursive call happens to 3 branches
# each are height N
def generateParenthesis(n: int) -> list[str]:
    if n == 0:
        return 
    if n == 1:
        return ['()']
    if n>1:
        return list(set([f'({x})' for x in generateParenthesis(n-1)] + [f'(){y}' for y in generateParenthesis(n-1)] + [f'{y}()' for y in generateParenthesis(n-1)]))
    
# effective backtracking solution 
# based on definition of valid parenthesis
# at each point, count open and close parenthesis
# add the total of each

def generateParenthesis(n: int) -> list[str]:
    stack = []
    ret = []

    def backtrack(nopen, nclose):
        # conditional backtracking allows for less conditionals
        # return cases

        if nclose==n:
            ret.append(''.join(stack))
            return
        
        # by definition, if nclose<nopen, there cnanot be any invalid arrangements
        if nclose<nopen:
            stack.append(')')
            backtrack(nopen, nclose+1)
            stack.pop()
        
        # only add nopen if it doesn't exceed max
        if nopen<n:
            stack.append('(')
            backtrack(nopen+1, nclose)
            stack.pop()

    backtrack(0,0)
    return ret


test = 3
print(generateParenthesis(test))