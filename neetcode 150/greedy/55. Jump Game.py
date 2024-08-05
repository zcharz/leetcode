# idea: 
# at each step, calculate the max it can reach
# if curr = max < end of list, return false


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        currmax = 0
        for ind, val in enumerate(nums):
            currmax = max(currmax, ind+val)
            if currmax >= len(nums)-1: return True
            if currmax == ind: return False
        # return True


sol = Solution()

nums = [2,3,1,1,4]
print(sol.canJump(nums))

nums = [3,2,1,0,4]
print(sol.canJump(nums))