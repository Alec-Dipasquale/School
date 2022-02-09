"""
Created by: Alec Dipasquale

"""
def decToBin(decimalNumber):
    #Add the largest 2^n that fits in decimal 
    #Add the next largest that fits in the remainder
    negative = False
    if decimalNumber<0:
        negative = True
        decimalNumber *= -1
    binList = []
    stringDecNumber = str(bin)
    remainder = decimalNumber
    for i in range(decimalNumber, -1, -1):
        if(2 ** i <= remainder):
            binList.append(i)
            remainder = remainder - (2**i)
        if i%5000 == 0:
            print(str(i/5000))
    result = 0
    for i in range(0, len(binList)):
        result = result + (10 ** (binList[i]))
    if negative:
        result *= -1
    return result


print(decToBin(281))