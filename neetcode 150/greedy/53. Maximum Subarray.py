class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        curr = 0

        for n in nums:
            if curr>0: curr+=n
            else: curr = n
            res = max(res, curr)
        return res
    

sol = Solution()

nums = [-1,0,-2]
print(sol.maxSubArray(nums))

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))

nums = [1]
print(sol.maxSubArray(nums))

nums = [5,4,-1,7,8]
print(sol.maxSubArray(nums))