def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    ret = []
    stack = []
    candidates.sort()

    def backtrack(curr, total):
        # needs to be in front in case last element== target
        # so that it doesnt get skipped by curr==len(canadidates)
        if total==target:
            ret.append(stack.copy())
            return

        if total>target or curr==len(candidates):
            return
        
        # pick current
        # continue to next, may be duplicate number but diff candidate 
        stack.append(candidates[curr])
        backtrack(curr+1, total+candidates[curr])
        stack.pop()

        # skip all instances of this element
        # to avoid duplicate number from diff candidate
        # below condition iterates curr to the last element of the duplicate
        # while curr + 1 < len(candidates) and candidates[curr] == candidates[curr + 1]:
        #     curr += 1
        # backtrack(curr+1, total)

        curr_num = candidates[curr]
        while curr<len(candidates) and candidates[curr] == curr_num:
            curr+=1
        backtrack(curr, total)
        
    backtrack(0, 0)
    return ret


candidates = [2,5,2,1,2]
target = 5

print(combinationSum2(candidates, target))