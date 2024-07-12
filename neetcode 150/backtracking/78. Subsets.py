class Solution:
    # recursive
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ret = []
        stack = []

        def dfs(n):
            if n==len(nums):
                ret.append(stack.copy())
                return
            
            # do nothing
            dfs(n+1)

            # add current number
            stack.append(nums[n])
            dfs(n+1)
            stack.pop()

        dfs(0)
        return ret


    # iterative
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ret = []
        stack = [([], 0)]

        while stack:
            curr, n = stack.pop()
            if n==len(nums):
                ret.append(curr)
                continue
            
            # if add nothing
            stack.append((curr.copy(), n+1))

            # if add current number
            copy = curr.copy()
            copy.append(nums[n])
            stack.append((copy, n+1))
        
        return ret


sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))