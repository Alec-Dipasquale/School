#returns a base 10 value that is representative of the binary value
def decToBin(decimalNumber):

    #Takes negative away and stores it for later
    negative = False
    if decimalNumber<0:
        negative = True
        decimalNumber *= -1
    
    binList = []
    stringDecNumber = str(bin)
    remainder = decimalNumber

    #Starts from the highest exponent of 2 that can fit into the remainder of
    #decimal number and then places them into a list
    for i in range(decimalNumber, -1, -1):
        if(2 ** i <= remainder):
            binList.append(i)
            remainder = remainder - (2**i)

    #Each exponenet stored is used on a base 10 and added together.
    result = 0
    for i in range(0, len(binList)):
        result = result + (10 ** (binList[i]))

    #Negative value is reapplied if applicable.
    if negative:
        result *= -1
    return result

num = 74
print("\n\nNumber: " + str(num))
print("Result: " + str(decToBin(num)) + "\n\n")