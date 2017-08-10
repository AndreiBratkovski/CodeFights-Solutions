"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

"""

def commonCharacterCount(s1, s2):
	
    global_count = 0
    
    char_count1 = 0
    char_count2 = 0
    
    s1_set = set(s1)
    
    
    for i in s1_set:
        if i in s2:
            char_count1 = s1.count(i)
            char_count2 = s2.count(i)
            
            if char_count1 <= char_count2:
                global_count += char_count1
            elif char_count2 <= char_count1:
                global_count += char_count2
                
    return global_count