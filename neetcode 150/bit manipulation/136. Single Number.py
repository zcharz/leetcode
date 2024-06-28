
# CONSTRAINTS:
# linear runtime -> one pass, can't sort
# constant extra space -> no extra data structures


# O(N) time, O(N) space
def singleNumber(nums: list[int]) -> int:
    d = dict()
    d[1] = set()
    d[2] = set()

    for n in nums:
        if n in d[1]:
            d[1].remove(n)
            d[2].add(n)
        else:
            d[1].add(n)
    
    return  d[1].pop()

# neetcode solution
# XOR can be done in any order
# since theres exactly 2 of each except one, each pair will XOR into 0
# each individual BIT will have 2 (or multiple of 2)
# resulting bits will equal the number without duplicate
def singleNumber(nums: list[int]) -> int:
    res = 0
    for n in nums:
        # ^ -> XOR
        res = n ^ res
    return res



test = [2,2,1]


print(singleNumber(test))