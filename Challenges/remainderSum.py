"""
Write a function that takes two integer inputs (int1 and int2) and returns the sum of the remainders for the following two Euclidean Division operations: int1 divided by int2 and int2 divided by int1.

In Euclidean division, the remainder is always greater than or equal to zero and also less than the absolute value of the divisor.

If the two inputs have different signs (i.e. one is positive and one is negative) you must ensure that the negative value is the dividend and the positive value is the divisor (i.e., if int1 = -10 and int2 = 7 then the two division operations would be -10 / 7 and -7 / 10.

If either input is equal to zero, return -1 as the result.

Example

For int1 = 3 and int2 = 2, the output should be
remainderSum(int1, int2) = 3.
The remainder of 3 / 2 is 1 and the remainder of 2 / 3 is 2, resulting in a sum of 3.

For int1 = -10 and int2 = 7, the output should be
remainderSum(-10, 7) = 7.
The remainder of -10 / 7 is 4 and the remainder of -7 / 10 is 3, resulting in a sum of 7.
"""
def remainderSum(int1, int2):

    if int1 == 0 or int2 == 0:
        return -1
    
    if int1 > 0 and int2 > 0:
        return (int1%int2 + int2%int1)
    
    if int1 < 0 and int2 < 0:
        return abs(int1%int2 + int2%int1)
    
    if int1 < 0 and int2 > 0:
        return (int1%int2 + (-int2)%(-int1))
    
    if int1 > 0 and int2 < 0:
        return ((-int1)%(-int2) + int2%int1)