class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r = r-1
            else:
                l = l+1
        return []
            

sol = Solution()

numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers, target))