from collections import defaultdict

def topKFrequent(nums: list[int], k: int) -> list[int]:

    count = defaultdict(int)
    for num in nums:
        count[num]+=1
    #O(n) count operation

    # same as above without using defaultdict
    # count = {}
    # for n in nums:
    #     count[n] = 1 + count.get(n, 0)


    nums_count = sorted(list(count.items()), key= lambda x: x[1], reverse=True)
    #O(nlogn) sorting operation

    ret = []
    for i in range(k):
        ret.append(nums_count[i][0])
    return ret
    
    #doable in O(n) with bucket sort


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))