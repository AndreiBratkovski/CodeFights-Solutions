"""
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".



"""

def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            first = i
        if s[i] == ")":
            last = i
            return reverseParentheses(s[:first] + s[first+1:last][::-1] + s[last+1:])
        
    return s