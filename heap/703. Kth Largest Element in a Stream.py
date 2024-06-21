import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapq.heapify(nums)

        while k<len(nums):
            heapq.heappop(nums)
        self.nums = nums


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        # initialization edge case with less elements in nums than k

        # min heap has min value at index 0
        # this is the kth largest
        return self.nums[0]
        
    

k = 3
nums = [4, 5, 8, 2]

test = KthLargest(k, nums)

add_list = [3,5,10,9,4]

for i in add_list:
    print(test.add(i))