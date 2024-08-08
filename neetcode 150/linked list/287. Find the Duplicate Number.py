# start at head, find loop using slow & fast pointer
# once loop is found, start start another pointer at head
# update original slow pointer and new slow pointer until they meet

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
    

sol = Solution()

nums = [1,3,4,2,2]
print(sol.findDuplicate(nums))

nums = [3,1,3,4,2]
print(sol.findDuplicate(nums))

nums = [3,3,3,3,3]
print(sol.findDuplicate(nums))