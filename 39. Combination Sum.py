def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    ret = []
    stack = []

    def backtrack(curr):
        # extra O(N) by using sum, could be reduced by using runnning sum
        if sum(stack)>target or curr==len(candidates):
            return

        if sum(stack)==target:
            ret.append(stack.copy())
            return
        
        # pick current
        # don't go next since same one can be picked multipel times
        stack.append(candidates[curr])
        backtrack(curr)
        stack.pop()

        # skip
        backtrack(curr+1)
    
    backtrack(0)

    return ret


test = [2,3,6,7]

print(combinationSum(test, 7))