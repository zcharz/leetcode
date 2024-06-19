def search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums)-1

    while start<=end:
        index = (start+end)//2
        # index = start+((end-start) // 2)

        element = nums[index]

        if target > element: start = index+1
        elif target < element: end = index-1
        else: return index
    return -1




test = [-1,0,3,5,9,12]
target = 9

print(search(test, target))

