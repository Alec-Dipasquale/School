def fpnToDec(fpnNum):
    negative = False
    if fpnNum[0] == '1':
        negative = True
    unsignedBinary = int(fpnNum[2:10])
    biasedExponent = binToDec(unsignedBinary)
    print(unsignedBinary)
    print(biasedExponent)
    index = 0
    for i in range(23):
        if fpnNum[len(fpnNum)-i-1] == '1':
            index = len(fpnNum)-i-1
            break
    leadingNormalized = fpnNum[11:index+1]
    unbiasedExponent = biasedExponent -127
    
    print (unbiasedExponent)
    print(fpnNum)
    print(leadingNormalized)
    print((float('1.' + str(leadingNormalized))))
    normalized = (float('1.' + str(leadingNormalized)) * (10**unbiasedExponent))
    print(normalized)
    decimalNumber = binToDec(int(normalized))
    if negative:
        decimalNumber *= -1
    return decimalNumber