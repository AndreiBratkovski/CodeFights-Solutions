"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

"""

def palindromeRearranging(inputString):
    
    pairs_list = []
    sortedString = ''.join(sorted(inputString))

    for i in range(0,len(sortedString)-1,2):
        if sortedString[i] == sortedString[i+1]:
            pairs_list.append((sortedString[i],sortedString[i+1]))
        
    if len(sortedString) % 2 == 0:
        if len(pairs_list) == (len(sortedString)//2):
            return True
        else:
            return False
        
    elif len(sortedString) % 2 != 0:
        if len(pairs_list) == ((len(sortedString)//2)) or len(pairs_list) %2 != 0:
            return True
        else:
            return False
                          
