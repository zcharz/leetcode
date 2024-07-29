class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ret = 0
        for n in nums:
            ret = ret ^ n
        return ret
    
sol = Solution()

nums = [2,2,1]
print(sol.singleNumber(nums))

nums = [4,1,2,1,2]
print(sol.singleNumber(nums))