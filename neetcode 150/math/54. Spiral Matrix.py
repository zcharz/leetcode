class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        ret = []

        while top<bottom and left<right:
            # add elements from top row
            for i in range(left,right+1):
                ret.append(matrix[top][i])
            # add elements from right column
            for i in range(top+1, bottom):
                ret.append(matrix[i][right])
            # add elements from bottom row
            for i in range(right,left-1, -1):
                ret.append(matrix[bottom][i])
            # add elements from left column
            for i in range(bottom-1, top, -1):
                ret.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if top == bottom:
            curr = [matrix[top][i] for i in range(left, right+1)]
            ret.extend(curr)
        elif left == right:
            curr = [matrix[i][left] for i in range(top, bottom+1)]
            ret.extend(curr)

        return ret


sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))
