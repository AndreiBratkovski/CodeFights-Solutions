"""
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
"""
def isCryptSolution(crypt, solution):
    numStr1 = []
    numStr2 = []
    numStr3 = []
    count = 0
    for word in crypt:
        for letter in word:
            for code in solution:
                if letter == code[0]:
                    if count == 0:
                        numStr1.append(code[1])
                    elif count == 1:
                        numStr2.append(code[1])
                    else:
                        numStr3.append(code[1])
        count += 1
        
        
    if len(numStr1) > 1 and numStr1[0] == "0":
        return False
    
    if len(numStr2) > 1 and numStr2[0] == "0":
        return False
    
    if len(numStr3) > 1 and numStr3[0] == "0":
        return False
    
    try:
        num1 = int(''.join(numStr1))
        num2 = int(''.join(numStr2))
        num3 = int(''.join(numStr3))
    
    except:
        return False
    
    if num1 + num2 == num3:
            return True
    
    return False
                    