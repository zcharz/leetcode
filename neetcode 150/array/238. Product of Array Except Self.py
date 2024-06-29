class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ret = [1]*length

        # storing prefix then postfix in output array
        # O(1) memory
        for i in range(length-1):
            ret[i+1] = ret[i]*nums[i]
        currpost = nums[-1]
        for i in range(length-2, -1, -1):
            ret[i]*=currpost
            currpost*=nums[i]
        return ret

        # storing prefix & postfix
        # O(n) memory
        prefix = [1]*(length)
        postfix = [1]*(length)

        for i in range(length-1):
            prefix[i+1] = prefix[i]*nums[i]
            postfix[length-i-2] = postfix[length-i-1]*nums[length-i-1]
        for i in range(length):
            ret[i] = prefix[i]*postfix[i]
        return ret

sol = Solution()

nums = [1,2,3,4]
print(sol.productExceptSelf(nums))

# nums = [-1,1,0,-3,3]
# print(sol.productExceptSelf(nums))