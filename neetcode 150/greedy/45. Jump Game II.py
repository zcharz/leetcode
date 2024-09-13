class Solution:
    def jump(self, nums: list[int]) -> int:
        steps = 0
        l = r = 0

        while r<len(nums)-1:
            maxnext = 0
            for i in range(l, r+1):
                maxnext = max(maxnext, i + nums[i])
            l = r+1
            r = maxnext
            steps+=1

        return steps

sol = Solution()

nums = [2,3,1,1,4]
print(sol.jump(nums))

nums = [2,3,0,1,4]
print(sol.jump(nums))

nums = [1,2]
print(sol.jump(nums))

nums = [4,1,1,3,1,1,1]
print(sol.jump(nums))
