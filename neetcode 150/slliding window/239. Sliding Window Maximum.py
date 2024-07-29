class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        curr = set(nums[0:k+1])
        ret = []

        for l in range(len(nums)-k+1):

            # HOW TO MAINTAIN MAX OR NEXT MAX IN O(1) TIME
            ret.append(max(nums[l:l+k]))

        return ret



sol = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums, k))

nums = [1]
k = 1
print(sol.maxSlidingWindow(nums, k))