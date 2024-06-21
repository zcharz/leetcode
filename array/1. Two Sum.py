
# O(n) time and space solution with dict
def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}  # val -> index

    for index, element in enumerate(nums):
        diff = target - element
        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[element] = index
