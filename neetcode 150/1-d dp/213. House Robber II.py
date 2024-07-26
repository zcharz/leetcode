class Solution:
    def rob(self, nums: list[int]) -> int:
        n1, n2, n3, n4 = 0, 0, 0, 0
        for i in range(len(nums)-1): n1, n2, n3, n4 = n2, max(n2, n1+nums[i]), n4, max(n4, n3+nums[i+1])
        return max(n2, n4, nums[0])


        # readable version below
        if len(nums) == 1:
            return nums[0]
        n1, n2, n3, n4 = 0, 0, 0, 0
        for n in nums[:len(nums)-1]:
            new = max(n2, n1+n)
            n1 = n2
            n2 = new 
        for n in nums[1:]:
            new = max(n4, n3+n)
            n3 = n4
            n4 = new
        return max(n2, n4)


sol = Solution()

nums = [2,3,2]
print(sol.rob(nums))

nums = [1,2,3,1]
print(sol.rob(nums))