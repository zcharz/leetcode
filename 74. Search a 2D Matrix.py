# solution must be O(log(m*n)) = O( log n + log m)

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    
    # row
    # O(log m) 
    while len(matrix)>1:
        m = len(matrix)//2

        if matrix[m][0]>target:
            matrix = matrix[:m]
        else:
            matrix = matrix[m:]
    
    matrix = matrix[0] # only 1 row, N columns left

    # O(log n)
    while len(matrix)>1:
        n = len(matrix)//2

        if matrix[n]>target:
            matrix = matrix[:n]
        elif matrix[n] == target:
            return True
        else:
            matrix = matrix[n:]
    
    if matrix[0] == target:
        return True
    return False


test = [[1],[3]]

print(searchMatrix(test, 3))