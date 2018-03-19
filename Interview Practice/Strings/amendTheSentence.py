"""
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
Example

For s = "CodefightsIsAwesome", the output should be
amendTheSentence(s) = "codefights is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello".
"""
def amendTheSentence(s):
    newstring = ""
    for index, element in enumerate(s):
        #
        # if element is capital
        # and not the first capital that appears
        # 
        if ord(element) < 97:
            if index != 0:
                newstring += ' '
            newstring += chr(ord(element)+32)
        else:
            newstring += element
    
    return newstring