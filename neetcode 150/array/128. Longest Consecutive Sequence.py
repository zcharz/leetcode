# must be in O(N) time

import heapq

def longestConsecutive(nums: list[int]) -> int:
    heapq.heapify(nums)
    # heapify is O(N)
    # note: O(N log N) if making N insertions
    # O(N) only based on vector implementations
    # using heapify assuming implementations are optimal

    sequences = []
    # list of lists for 

    if not nums:
    # if nums is empty
    # edge case
        return 0

    curr = heapq.heappop(nums)
    seq = [curr]
    # start of the first sequence

    while len(nums)!=0:
        next = heapq.heappop(nums)

        if next == curr+1:
            seq.append(next)
        elif next == curr:
            continue
        else:
            sequences.append(seq)
            seq = [next]
        curr = next
    
    sequences.append(seq)

    return len(max(sequences, key=lambda x: len(x)))
    # key -> x is each individual element
    # max returns element, which is a list


# neetcode solution
# same idea, but with a set
# check every item to see if it has a left element O(N)
# if it does, it is the start of a sequence
def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


# test = [100,4,200,1,3,2]
# test = [0,3,7,2,5,8,4,6,0,1]
test = [1,2,0,1]

print(longestConsecutive(test))

