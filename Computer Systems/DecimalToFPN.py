import BinaryToDecimal

#converts a decimal number into a 32 bit FPN
def decToFpn(decimalNumber):
    #adds significant digit
    if decimalNumber<0:
        fpn = "1 "
        decimalNumber *= -1
    else:
        fpn = "0 "
    
    binary = decToBin(decimalNumber)
    binList = [int(x) for x in str(binary)]
    #adds the us
    unbiasedExponent = len(binList)-1
    biasedExponent = 127 + unbiasedExponent
    unsignedBinary = decToBin(biasedExponent)
    fpn += str(unsignedBinary) + " "
    binary = int(str(binary)[0 : 0 : ] + str(binary)[0 + 1 : :])
    fpn += str(binary)
    for i in range(32 -len(fpn)):
        fpn += "0"
    return fpn

print(decToFpn(2015))