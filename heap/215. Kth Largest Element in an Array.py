# solve without sorting

import heapq


# O(k log N) time complexity solution using heap
# O(1) extra memory
def findKthLargest(nums: list[int], k: int) -> int:
    nums = [-n for n in nums]

    heapq.heapify(nums)

    for i in range(k-1):
        heapq.heappop(nums)
    return -1*heapq.heappop(nums)


# neetcode solution
# O(N) average case quick select
# O(N^2) worst case
# O(1) extra space complexity

def partition(nums: list[int], left: int, right: int) -> int:
    pivot, fill = nums[right], left

    for i in range(left, right):
        if nums[i] <= pivot:
            nums[fill], nums[i] = nums[i], nums[fill]
            fill += 1

    nums[fill], nums[right] = nums[right], nums[fill]

    return fill

def findKthLargest(nums: list[int], k: int) -> int:
    k = len(nums) - k
    left, right = 0, len(nums) - 1

    while left < right:
        pivot = partition(nums, left, right)

        if pivot < k:
            left = pivot + 1
        elif pivot > k:
            right = pivot - 1
        else:
            break

    return nums[k]