class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # at any given point, 
        # how many numbers are smaller than the current

        ret = 1
        start, end = 0, 1

        while end<len(nums):
            if nums[end] <= nums[end-1]:
                start = end
                end = end+1
            else:
                ret = end - start
                end+=1

        return ret


nums = [10,9,2,5,3,7,101,18]
sol = Solution()

print(sol.lengthOfLIS(nums))