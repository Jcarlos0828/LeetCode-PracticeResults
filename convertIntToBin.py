import math

def strToBin(number):
    myInt = int(number)
    exponentInt = math.sqrt(myInt)
    exponentInt = math.floor(exponentInt)
    exponent = 2 ** exponentInt
    binaryChars = []
    while exponentInt >= 0:
        if myInt - exponent >= 0:
            #0 - 1
            myInt = myInt - exponent
            binaryChars.append('1')
        else:
            binaryChars.append('0')
        print(exponentInt)
        print(exponent)
        exponentInt = exponentInt - 1
        exponent = 2 ** (exponentInt)
    return "".join(binaryChars)

print(strToBin(93))