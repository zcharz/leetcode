class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l1, l2 = 0, 0 
        r1, r2 = len(nums1)-1, len(nums2)-1

        def findMedian(arr, l, r):
            m = (l+r)//2
            if (l+r+1)%2 == 0:
                return (arr[m]+arr[m+1])/2
            return arr[m]

        while l1<=r1 or l2<=r2:
            m1 = (l1+r1)//2
            m2 = (l2+r2)//2

            # bruteforce when range is small enough 
            if r1-l1<3 and r2-l2<3:
                print('bruteforce')
                temp = [i for i in nums1[l1:r1+1]]
                temp.extend([i for i in nums2[l2:r2+1]])
                temp.sort()
                print(temp)
                return findMedian(temp, 0, len(temp)-1)
                

            if l1<=r1 and l2<=r2:
                if nums1[m1]<=nums2[m2]:
                    l1 = m1+1
                    r2 = m2
                else:
                    l2 = m2+1
                    r1 = m1
            elif l1<=r1:
                return findMedian(nums1, l1, r1)
            else:
                return findMedian(nums2, l2, r2)
            


sol = Solution()

nums1 = [1,3]
nums2 = [2]
print(2, sol.findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(2.5, sol.findMedianSortedArrays(nums1, nums2))

nums1 = [2]
nums2 = []
print(2, sol.findMedianSortedArrays(nums1, nums2))

nums1 = [0,0,0,0,0]
nums2 = [-1,0,0,0,0,0,1]
print(0, sol.findMedianSortedArrays(nums1, nums2))

nums1 = [1,2,3,4]
nums2 = []
print(2.5, sol.findMedianSortedArrays(nums1, nums2))

nums1 = [1,2,3,4]
nums2 = [5]
print(3, sol.findMedianSortedArrays(nums1, nums2))