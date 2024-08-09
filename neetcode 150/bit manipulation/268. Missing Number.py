# bit manipulation using XOR
# [0, 3, 1] ^ [0, 1, 2, 3] -> 2

# sum(0 to n) - sum(nums)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # bit manipulation method
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res

    
        # sum method
        res = len(nums)
        for i in range(len(nums)):
            res = res + i - nums[i]
        return res

sol = Solution()

nums = [3,0,1]
print(sol.missingNumber(nums))

nums = [0,1]
print(sol.missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(sol.missingNumber(nums))