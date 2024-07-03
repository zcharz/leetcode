# algorithm must be in O(n) time

# O(n) solution: 
# check length of sequence (by iterating)
# ONLY when curr is the start of a sequence
# where curr-1 doesn't exist
# this checking is TOTAL O(n) time and occurs only once

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ret = 0
        nums = set(nums)

        for i in nums:
            if i-1 in nums: continue

            curr, count = i+1, 1
            while curr in nums: 
                count+=1
                curr+=1
            ret = max(count, ret)

        return ret
    

sol = Solution()

nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))