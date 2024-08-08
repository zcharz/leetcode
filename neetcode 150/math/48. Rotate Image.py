class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for offset in range(n//2):
            for ind in range(offset, n-offset-1):
                val1 = matrix[offset][ind]
                val2 = matrix[ind][n-offset-1]
                val3 = matrix[n-offset-1][n-ind-1]
                val4= matrix[n-ind-1][offset]
                # print(val1, val2, val3, val4)

                matrix[offset][ind] = val4
                matrix[ind][n-offset-1] = val1
                matrix[n-offset-1][n-ind-1] = val2
                matrix[n-ind-1][offset] = val3


sol = Solution()

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
# sol.rotate(matrix)
# for row in matrix:
#     print(row)

matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]]
sol.rotate(matrix)
for row in matrix:
    print(row)