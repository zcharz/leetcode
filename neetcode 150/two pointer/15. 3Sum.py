# [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k
# nums[i] + nums[j] + nums[k] == 0

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ret = []

        for i, val in enumerate(nums):
            if i>0 and val == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1
            target = 0-nums[i]

            while j<k:
                curr = nums[j]+nums[k]
                if curr<target:
                    j+=1
                elif curr>target:
                    k-=1
                else:
                    ret.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
        return ret



sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

nums = [3,0,-2,-1,1,2]  
print(sol.threeSum(nums))

