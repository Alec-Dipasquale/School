import DecimalToBinary

#converts a decimal number into a 32 bit FPN
def decToFpn(decimalNumber):
    #adds significant digit
    if decimalNumber<0:
        fpn = "1 "
        decimalNumber *= -1
    else:
        fpn = "0 "
    
    binary = DecimalToBinary.decToBin(decimalNumber)
    binList = [int(x) for x in str(binary)]

    #puts the 11 bit exponent, created from 127 bias, into the string 
    unbiasedExponent = len(binList)-1
    biasedExponent = 127 + unbiasedExponent
    unsignedBinary = DecimalToBinary.decToBin(biasedExponent)
    fpn += str(unsignedBinary) + " "

    #Adds the 23 bit Mantissa to the string
    binary = int(str(binary)[0 : 0 : ] + str(binary)[0 + 1 : :])
    fpn += str(binary)
    for i in range(32 -len(fpn)):
        fpn += "0"
    return fpn


num = -205
print("\n\nNumber: " + str(num))
print("Result: " + str(decToFpn(num)))