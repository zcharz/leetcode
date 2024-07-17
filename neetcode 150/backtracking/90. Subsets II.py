class Solution:
    # recursive solution
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        ret = []
        stack = []
        
        def dfs(n):
            if n == len(nums):
                ret.append(stack.copy())
                return
            
            # choose to take current
            stack.append(nums[n])
            dfs(n+1)
            stack.pop()

            # choose to skip current and all copies of it
            while n+1<len(nums) and nums[n] == nums[n+1]:
                n+=1
            dfs(n+1)

        dfs(0)
        return ret
    
    # iterative solution
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        ret = []
        stack = [([], 0)]

        while stack:
            curr, n = stack.pop()
            if n == len(nums):
                ret.append(curr)
                continue

            # if add current number
            copy = curr.copy()
            copy.append(nums[n])
            stack.append((copy, n+1))

            # if add nothing
            while n+1<len(nums) and nums[n] == nums[n+1]:
                n+=1
            stack.append((curr.copy(), n+1))
        
        return ret


sol = Solution()
nums = [1,2,2]
print(sol.subsetsWithDup(nums))
        