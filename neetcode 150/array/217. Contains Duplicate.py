class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(nums))

nums = [1,2,3,4]
print(sol.containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums))