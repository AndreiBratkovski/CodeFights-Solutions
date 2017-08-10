"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

"""

def sortByHeight(a):
    trees = []
    people = []
    newList = [None] * (len(a))
    
    for i in range(len(a)):
        if a[i] == -1:
            trees.append(i)
        else:
            people.append(a[i])
    
    for i in trees:
        newList[i] = -1
        
    people = sorted(people)
    
    count = 0
    for i in range(len(newList)):
        if newList[i] == -1:
            continue
        else:
            newList[i] = (people[count])
            count +=1
            
    return newList