"""
Given a matrix (i.e. an array of arrays), find its submatrix obtained by deleting the specified rows and columns.

Example

For

matrix = [[1, 0, 0, 2], 
          [0, 5, 0, 1], 
          [0, 0, 3, 5]]
rowsToDelete = [1] and columnsToDelete = [0, 2], the output should be

constructSubmatrix(matrix, rowsToDelete, columnsToDelete) = [[0, 2],
                                                             [0, 5]]
"""
def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    if len(rowsToDelete) > 0:
        for num in rowsToDelete:
            matrix.remove(matrix[num])
    
    print(matrix)
    
    prevNum = 30
    if len(columnsToDelete) > 0:
        for num in columnsToDelete:
            for lst in matrix:
                lst[num] = "terminate"
    
    print(matrix)
                    
    for lst in matrix:
        for element in lst:
            if element == "terminate":
                lst.remove(element)
                
    return matrix