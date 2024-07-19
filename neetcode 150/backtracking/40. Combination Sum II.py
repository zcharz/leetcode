class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ret = []
        stack = []

        def dfs(n, currsum):
            if currsum == target:
                ret.append(stack.copy())
                return
            elif n == len(candidates) or currsum > target:
                return
            
            # take
            stack.append(candidates[n])
            dfs(n+1, currsum+candidates[n])
            stack.pop()

            # don't take (and don't take any future copies)
            while n+1<len(candidates) and candidates[n] == candidates[n+1]:
                n+=1
            dfs(n+1, currsum)

        dfs(0, 0)
        return ret



sol = Solution()

candidates = [10,1,2,7,6,1,5]
target = 8
print(sol.combinationSum2(candidates, target))