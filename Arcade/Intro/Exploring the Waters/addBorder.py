"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

"""

def addBorder(picture):
    
    for i in range(len(picture)):
        picture[i] = ("*" + picture[i] + "*")
    
    borderLength = len(picture[0])
    picture.insert(0, ("*" * borderLength))
    picture.insert((len(picture)+1),("*"*(borderLength)))
    
    return picture