class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2
            # left portion is rotated and sorted
            if nums[mid]>nums[r]:
                # target has to be on right (not in left sorted portion)
                if target<nums[l] or nums[mid]<target: l = mid+1
                else: r = mid
            # right portion is sorted
            # once entire search area (subarray) is sorted, only else is ran
            # effectively the same as normal binary search
            else:
                # target is in right sorted portion (excluding mid)
                if nums[mid]<target<=nums[r]: l = mid+1
                # target is not in right sorted portion
                else: r = mid
        return l if nums[l] == target else -1



sol = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
print(sol.search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(sol.search(nums, target))