import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False

        count = dict()
        for i in hand:
            count[i] = count.get(i,0)+1

        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            start = minheap[0]

            for i in range(start, start+groupSize):
                if i not in count: return False

                count[i] -= 1
                if count[i] == 0:
                    if i != minheap[0]: return False
                    heapq.heappop(minheap)
        return True


sol = Solution()

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(sol.isNStraightHand(hand, groupSize))

hand = [1,2,3,4,5]
groupSize = 4
print(sol.isNStraightHand(hand, groupSize))