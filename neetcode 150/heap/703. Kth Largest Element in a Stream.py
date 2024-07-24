import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


nums = [4, 5, 8, 2]
sol = KthLargest(3, nums)
print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))