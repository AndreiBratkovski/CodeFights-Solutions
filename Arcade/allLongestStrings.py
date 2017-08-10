"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

"""

def allLongestStrings(inputArray):
	
    longest = 0
    longest_strings = []
    
    for i in inputArray:
        if len(i) > longest:
            longest = len(i)
            
    for i in inputArray:
        if len(i) == longest:
            longest_strings.append(i)
            
    return longest_strings

