from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ret = []
        queue = deque()
        l = r = 0

        while r<len(nums):

            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if l > queue[0]: queue.popleft()
            
            if (r + 1) >= k: 
                ret.append(nums[queue[0]])
                l+=1
            r+=1

        return ret



sol = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums, k))

nums = [1]
k = 1
print(sol.maxSlidingWindow(nums, k))