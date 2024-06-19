def lastStoneWeight(stones: list[int]) -> int:

    while len(stones)>1:
        x = max(stones)
        stones.remove(x)
        y = max(stones)
        stones.remove(y)

        new = abs(x-y)
        if new:
            # if new != 0
            stones.append(new)

    if stones:
        # if stones != []
        return stones[0]
    return 0



# using heaps
# each add is  O(log n)
# each max is O(1)
# compared to ead max being O(n)

import heapq

def lastStoneWeight(stones: list[int]) -> int:

    # using a min heap, reverse all values
    stones = [-s for s in stones]
    heapq.heapify(stones)
    # stones is now a heapq object

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)
            #push first - second into stones

    # edge case for if stones is empty
    stones.append(0)
    return abs(stones[0])