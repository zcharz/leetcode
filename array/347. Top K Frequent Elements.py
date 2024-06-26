import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = dict()

        # O(n) time
        for i in nums:
            count[i] = count.get(i, 0)+1

        # BUCKET SORT SOLUTION -> O(n)
        # making bucket -> O(n)
        # finding top k -> O(n)
        bucket = [[] for i in range(len(nums))]
        for key, val in count.items():
            bucket[val-1].append(key)

        ret = []
        for i in range(len(nums)-1, -1, -1):
            ret.extend(bucket[i])
            if len(ret) ==k:
                return  ret
        

        # HEAP SOLUTION -> O(n+klogn)
        # heapify -> O(n) time
        # heappop -> O(logn) time, called k times
        heapcount = [(-val, key) for key, val in count.items()]
        heapq.heapify(heapcount)
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heapcount)[1])
        return ret

        # SORTING SOLUTION -> O(nlogn)
        sortcount = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sortcount][:k]
    

sol = Solution()

nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))

nums = [1]
k = 1
print(sol.topKFrequent(nums, k))