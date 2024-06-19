# since houses are arranged in a circle
# cannot take 1st and last one both
# using normal dp, a solution taking both would be invalid
# however if the solution only took one or took none it would be valid


# how to avoid this scenario?
# do normal dp on 0-len-2, 1-len-1
# iif solution would not take one or none, it would return the same solution anyway

# this creates an edge case if len = 1



def rob(nums: list[int]) -> int:

    if len(nums) ==1:
        return nums[0]


    rob1, rob2 = 0, 0    

    # doesnt include last element
    for i in range(len(nums)-1):
        temp = max(rob1+nums[i], rob2)
        rob1 = rob2
        rob2 = temp

    iter1 = rob2

    rob1, rob2 = 0, 0
    
    for i in range(1,len(nums)):
        temp = max(rob1+nums[i], rob2)
        rob1 = rob2
        rob2 = temp

    iter2 = rob2

    return max(iter1, iter2)




def robOld(nums: list[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


test = [2,3,2]


print(rob(test))
print(robOld(test))



# neetcode solution
# more concise, pythonic code
# using helper function to reduce overall lines
# use max to skip edge case

def rob(nums: list[int]) -> int:
    def helper( nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
