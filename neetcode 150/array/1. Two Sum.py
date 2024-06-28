class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, number in enumerate(nums):
            complement = target-number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index


sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))