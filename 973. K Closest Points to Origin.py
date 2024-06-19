import math


# O(N log N) solution using  sort
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    #calculate distance for every point
    #dist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
   
    return sorted(points, key = lambda x: math.sqrt((x[0])**2 + (x[1])**2))[:k]

# can be reduced to
# O(K log N) using heap
# since heapify is O(N)
# pop k times
# each pop is log N time

# note that retriving the min/max value is O(1)
# popping requires reordering the heap, takes log N time

# neetcode solution
import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    minheap = []
    for x, y in points:
        minheap.append([x**2+y**2, x, y])
    heapq.heapify(minheap)

    ret = []

    for i in range(k):
        point = heapq.heappop(minheap)
        ret.append([point[1], point[2]])
    return ret