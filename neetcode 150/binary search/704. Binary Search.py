class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # step method
        # finds the spot where values greater than or equal to start appearing
        # if the target exists, it will necessarily be at the first spot
        # which is where l == r are at after the iteration
        l, r = 0, len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        return l if nums[l] == target else -1
    
        # normal method (checking target)
        # l<r needs to start at len(nums)
        # in case all numbers are below target
        l, r = 0, len(nums)
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid #(r = mid-1 DOES NOT WORK)
        return -1

        # l<=r needs r to start at len(nums)-1
        # in case target is at the end
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1   #(r = mid DOES NOT WORK)
        return -1



sol = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(sol.search(nums, target))