class Solution:
    def jump(self, nums: list[int]) -> int:
        count, pos = 0, 0

        while pos < len(nums)-1:
            currdist = 0
            ind = 0
            for i in range(pos+1, nums[pos]+1):
                if i+nums[i]> currdist: 
                    currdist = i+nums[i]
                    ind = i
            count+=1
            pos = ind

        return count

sol = Solution()

nums = [2,3,1,1,4]
print(sol.jump(nums))

nums = [2,3,0,1,4]
print(sol.jump(nums))

nums = [1,2]
print(sol.jump(nums))