"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.



"""

def addTwoDigits(n):
    total = 0
    n = [int(i) for i in str(n)]
    for i in n:
        total += i
    
    return total