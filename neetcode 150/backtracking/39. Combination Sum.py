class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        stack = []
        ret = []

        def dfs(ind, curr):
            if ind>=len(candidates) or curr>target:
                return

            if curr==target:
                ret.append(stack.copy())
                return
        
            # add current and continue:
            stack.append(candidates[ind])
            dfs(ind, curr+candidates[ind])
            stack.pop()
            
            # don't add current
            dfs(ind+1, curr)

        dfs(0, 0)
        return ret


sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates, target))