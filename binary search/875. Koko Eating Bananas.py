import math

class Solution:
    # using binary search to find the minimum value of k
    # which ranges between 1 and the max value of piles
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # determines if bananas can be finished 
        # given current eating speed (curr)
        def canFinish(k):
            time = 0
            for banana in piles:
                time+=math.ceil(banana/k)
            return time<=h

        l, r = 1, max(piles)
        while l<r:
            mid = (l+r)//2
            if not canFinish(mid): # if nums[mid] < target: 
                l = mid+1
            else:
                r = mid
        return l
    
        # step method 
        # l=r at first value of k that canFinish
        # - any lower values of k cannot finish in <h hours, thus shift left to mid+1
        # - any higher or equal value shift right down to mid, 
        #   since current mid maybe smallest 
    

sol = Solution()

piles = [3,6,7,11]
h = 8
print(sol.minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 5
print(sol.minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 6
print(sol.minEatingSpeed(piles, h))