class Solution:
    def rob(self, nums: list[int]) -> int:
        l, r = 0, nums[0]
        for i in range(1, len(nums)):
            l, r = r, max(l+nums[i], r)
        return r

sol = Solution()

nums = [1,2,3,1]
print(sol.rob(nums))

nums = [2,7,9,3,1]
print(sol.rob(nums))

nums = [2,1,1,2]
print(sol.rob(nums))