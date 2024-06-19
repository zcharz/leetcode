# logic: 
# since we don't need to return the indicies
# just have a O(n) one pass keeping the max sum of previous elements
# if elements are negative, reset to 0 (signifiying not counting the elements in the subarray)

def maxSubArray(nums: list[int]) -> int:
    max_ret = nums[0]
    curr_sum = 0

    for i in nums:
        if curr_sum < 0:
            curr_sum = 0
        currSum += i

        max_ret = max(curr_sum, max_ret)

    return max_ret


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(maxSubArray(nums))