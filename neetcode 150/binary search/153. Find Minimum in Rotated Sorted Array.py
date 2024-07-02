class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]


sol = Solution()

nums = [3,4,5,1,2]
print(sol.findMin(nums))

nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums))

nums = [11,13,15,17]
print(sol.findMin(nums))