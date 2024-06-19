
# theory:
# brute force iteration: O(N^2)
# sorted iteration: O(N log N)

#     How can we prove that at least one duplicate number must exist in nums?
#     - pigeonhole princple

# linear time solution
# floyd's cycle detection/tortise and hare 


# element as number its pointing to
# since indexes are unique and elements may not be
# 


def findDuplicate(nums: list[int]) -> int:
    
    # 0 is not part of the cycle for sure 
    # since numbers are [1,n]
    p1, p2 = 0, 0

    while True:
        p1 = nums[p1]
        p2 = nums[nums[p2]]
        if p1 == p2:
            break

    # use second slow pointer,
    # when increment both slow pointers
    # when both meet, that is the start of the loop
    p3 = 0
    while True:
        p1 = nums[p1]
        p3 = nums[p3]
        if p1 == p3:
            return p1


# nums = [2,5,9,6,9,3,8,9,7,1]
nums = [3,1,3,4,2,5]

print(findDuplicate(nums))