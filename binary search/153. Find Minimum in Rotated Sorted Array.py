def findMin(nums: list[int]) -> int:
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
            return nums[bruteforce(l, mid, r)]

        if n1<n2<n3:
            # done
            return nums[l]
        elif n1>n2:
            # pivot is betweenj l and mid
            r = mid
        elif n2>n3:
            # pivot is between mid and r
            l = mid