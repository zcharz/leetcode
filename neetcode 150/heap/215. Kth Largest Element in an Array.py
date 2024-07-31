import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while k-1:
            heapq.heappop(nums)
            k-=1
        return -nums[0]


sol = Solution()

nums = [3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(sol.findKthLargest(nums, k))