"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

"""

def bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

    
def almostIncreasingSequence(sequence):
    k = bad_pair(sequence)
    if k == -1:
        return True
    
    if bad_pair(sequence[k-1:k] + sequence[k+1:]) == -1:
        return True
    
    if bad_pair(sequence[k:k+1] + sequence[k+2:]) == -1:
        return True
    
    return False