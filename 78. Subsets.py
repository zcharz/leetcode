# since list is unique, sort doesnt matter
# just iterate once through each element
# as a different starting point

# pseudo code:
# for each length, 
# backtrack: 
#   add n
#   recursive backtrack on that element
#   pop n


def subsets(nums: list[int]) -> list[list[int]]:
    ret = []
    stack = []

    def backtrack(curr):
        if curr==len(nums):
            ret.append(stack.copy())
            return
        
        stack.append(nums[curr])
        backtrack(curr+1)
        stack.pop()
        
        backtrack(curr+1)
    
    backtrack(0)

    return ret

test = [1,2,3]
print(subsets(test))