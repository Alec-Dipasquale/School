import BinaryToDecimal
def fpnToDec(fpnNum):
    #takes the significant digit and stores negative for the end.
    negative = False
    if fpnNum[0] == '1':
        negative = True
    #takes the Exponent portion of fpn and converts it to decimal
    unsignedBinary = int(fpnNum[2:10])
    biasedExponent = BinaryToDecimal.binToDec(unsignedBinary)
    
    #Gets the index of the end of the normalized decimal within the 23 bit Mantissa
    index = 0
    for i in range(23):
        if fpnNum[len(fpnNum)-i-1] == '1':
            index = len(fpnNum)-i-1
            break
    
    #create normalized binary number and then convert it from binary to decimal.
    leadingNormalized = fpnNum[11:index+1]
    unbiasedExponent = biasedExponent -127
    normalized = (float('1.' + str(leadingNormalized)) * (10**unbiasedExponent))
    decimalNumber = BinaryToDecimal.binToDec(int(normalized))
    
    #Adds final negative sign if needed.
    if negative:
        decimalNumber *= -1

    return decimalNumber

fpn = "1 10000110 100110100000000000000"
print("\n\nFPN: " + str(fpn))
print("Result: " + str(fpnToDec(fpn)))