"""
Given an integer size, return an array containing each integer from 1 to size in the following order:

1, size, 2, size - 1, 3, size - 2, 4, ...

Example

For size = 7, the output should be
constructArray(size) = [1, 7, 2, 6, 3, 5, 4].

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer size

A positive integer.

Guaranteed constraints:
1 ≤ size ≤ 15.

[output] array.integer
"""
def constructArray(size):
    arr = []
    origSize = size
    for i in range(1,8):
        arr.append(i)
        if len(arr) == origSize:
            break
        arr.append(size)
        if len(arr) == origSize:
            break
        size -= 1
    
    return arr

