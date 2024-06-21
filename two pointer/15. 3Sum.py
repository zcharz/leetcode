# sort in order to skip impossible matches
# iterate to count one element
# 2 pointer on remaining elements

def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    ret = []

    for i in range(len(nums)-2):
        # if the starting, minuimum value is greater than 0, sum cannot equal to 0
        if nums[i]>0:
            break
        if i>0 and nums[i] == nums[i-1]:
            continue
            
        start, end = i+1, len(nums)-1
        while start<end:
            sum = nums[i]+ nums[start] + nums[end]
            if sum>0: end-=1
            elif sum<0: start+=1
            else:
                ret.append([nums[i], nums[start], nums[end]])
                start+=1
                end-=1
                # avoidning duplicate solutions by skipping all duplicates of end
                while nums[end]==nums[end+1] and start<end:
                    end-=1
    return ret



test = [-1,0,1,2,-1,-4]
test = [3,0,-2,-1,1,2]  

print(threeSum(test))


# neetcode solution
def threeSum(nums: list[int]) -> list[list[int]]:

    res = []
    nums.sort()

    for i, a in enumerate(nums):
        # Skip positive integers
        if a > 0:
            break

        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res


