def productExceptSelf(nums: list[int]) -> list[int]:
    left = [1]
    right = [1]

    l = 1
    r = 1
    for i in range(len(nums)):
        l*=nums[i]
        r*=nums[len(nums)-1-i]
        left.append(l)
        right.insert(0, r)
    
    # print(left)
    # print(right)

    ret = []
    for i in range(len(nums)):
        ret.append(left[i]*right[i+1])

    return ret



# neetcode solution 
# O(N) space solution
# store prefix in output array
# multiply postfix in second iteration into output array directly
# store postfix each time for next iteration
def productExceptSelf(self, nums: list[int]) -> list[int]:
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res



test = [1,2,3,4]

print(productExceptSelf(test))