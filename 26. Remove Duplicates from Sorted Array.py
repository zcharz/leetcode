def removeDuplicates(nums: list[int]) -> int:
    i = 0
    while i < len(nums)-1:
        print(nums, i)
        if nums[i] == nums[i+1]:
            nums.pop(i)
            i =- 1
        i += 1

    return len(nums)

if __name__ == '__main__':
    l = [0,0,1,1,1,2,2,3,3,4]
    print(str(l) + ' = ' + str(removeDuplicates(l)))