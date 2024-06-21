def rob(nums: list[int]) -> int:
    dp = [0 for i in nums]

    if len(nums)<3:
        return max(nums)
    
    # len(nums) > 2
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2,len(dp)):
        dp[i] = max( (dp[i-2] + nums[i]) , dp[i-1])
    
    return dp[-1]



test = [1,2,3,1]

print(rob(test))



# neetcode solution
# O(1) additional memory

def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2