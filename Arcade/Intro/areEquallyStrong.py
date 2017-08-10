"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15 and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 9, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.

"""

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStrongest = 0
    yourWeakest = 0
    
    friendsStrongest = 0
    friendsWeakest = 0
    yourStrongest = 0
    
    if yourLeft > yourRight:
        yourStrongest = yourLeft
        yourWeakest = yourRight
    else:
        yourStrongest = yourRight
        yourWeakest = yourLeft
        
    if friendsLeft > friendsRight:
        friendsStrongest = friendsLeft
        friendsWeakest = friendsRight
        
    else:
        friendsStrongest = friendsRight
        friendsWeakest = friendsLeft
        
    yourStrength = yourLeft + yourRight
    friendStrength = friendsLeft + friendsRight
    totalStrength = (yourStrength + friendStrength)/2
    
    if yourStrength == friendStrength:
        if friendsStrongest != yourStrongest or friendsWeakest != yourWeakest:
            return False
        else:
            return True
    else:
        return False
                          
