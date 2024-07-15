class Solution:
    # recursive swapping solution
    def permute(self, nums:list[int]) -> list[list[int]]:
        ret = []

        def dfs(i):
            if i==len(nums):
                ret.append(nums.copy)
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return ret

    # recursive neetcode solution
    # same idea as swap, recursively calling subproblems without the curreent number
    def permute(self, nums: list[int]) -> list[list[int]]:
        ret = []
        if len(nums)==1: return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for p in perms:
                p.append(n)
            ret.extend(perms)
            nums.append(n)

        return ret
    

sol = Solution()

nums = [1, 2, 3]
print(sol.permute(nums))