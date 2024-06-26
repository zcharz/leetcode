# solution needs to be O(log(m*n))

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = 0
        while l<=r:
            mid = (l+r)//2
            # target is necessarily between the current row range,
            # below, or above
            if matrix[mid][0]<=target<=matrix[mid][len(matrix[0])-1]:
                row = mid
                break
            elif matrix[mid][0]>target:
                r=mid-1
            else: #matrix[mid][len(matrix[0])-1] < target
                l=mid+1

        l, r = 0, len(matrix[0])-1
        while l<r: 
            mid = (l+r)//2
            if matrix[row][mid]<target:
                l = mid+1
            else:
                r = mid
        return matrix[row][l]==target
    

sol = Solution()



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(sol.searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))

matrix = [[1],[3]]
target = 3
print(sol.searchMatrix(matrix, target))

matrix = [[1],[3]]
target = 5
print(sol.searchMatrix(matrix, target))