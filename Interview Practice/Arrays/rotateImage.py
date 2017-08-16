"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

"""

import copy

def rotateImage(a):
    b = copy.deepcopy(a)
    
    for i in range(len(a)):
        count = 0
        for k in range(len(a))[::-1]:
            b[i][count] = a[k][i]
            count +=1
    return b