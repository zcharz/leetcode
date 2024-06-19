
# O(2 log N) solution using find pivot
# two pass
# same as 153. Find Minimum in Rotated Sorted Array

def search(nums: list[int], target: int) -> int:
    pivot = findPivot(nums)    

    # binary search
    start, end = 0, len(nums)-1

    while start<=end:
        index = (start+end)//2
        # index = start+((end-start) // 2)

        element = nums[(index+pivot)%len(nums)]

        if target > element: start = index+1
        elif target < element: end = index-1
        else: return (index+pivot)%len(nums)
    return -1


def findPivot(nums):
    # find min value in log N time
    l, r = 0, len(nums)-1

    def bruteforce(l, mid, r):
    # brute force at len 3 or less
        n1, n2, n3 = nums[l], nums[mid], nums[r]

        if r-l == 0:
            return r

        # len 2
        if r-l==1: 
            if n1 < n3:
                return l
            else:
                return r
            
        # len 3
        if n1>n2:
            return mid
        elif n2>n3:
            return  r
        else:
            return l

    while l<=r:
        mid = (l+r)//2
        n1, n2, n3 = nums[l], nums[mid], nums[r]

        if r-l<3:
            return bruteforce(l, mid, r)

        if n1<n2<n3:
            # done
            return l
        elif n1>n2:
            # pivot is betweenj l and mid
            r = mid
        elif n2>n3:
            # pivot is between mid and r
            l = mid
    
    
test1 = [4,5,6,7,8,1,2,3]
test2 = [4,5,6,7,0,1,2]
print(findPivot(test1))

print(test1)
print(search(test1, 8))



# neetcode solution 
# O(log N)
# one pass

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

