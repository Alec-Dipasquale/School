#
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

def binToDec(binaryNumber):
    #Get the place of each '1' in the binary digit
    #get the product of (2^ ('1's placement)
    #Add each of those placements together 
    negative = False
    if binaryNumber<0:
        negative = True
        binaryNumber *= -1
    result = 0
    #get each binary digit's position
    stringBinNumber = str(binaryNumber)
    digits = list(stringBinNumber)
    digits.reverse()
    #puts positions in decList. Example decList = [4,2,0]
    for i in range(len(digits)):
        if(digits[i] == '1'):
            result = result +(2 ** i)
        if i%500 == 0:
            print(i/500)
    if negative:
        result *= -1
    return result

def switchDecToHex(num):
    switcher = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    return switcher.get(num, num)

def switchHexToDec(num):
    switcher = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    return switcher.get(num, num)

def decToHex(decimalNumber):
    #store each digit in array 
    #divide by 16 get remainder 
    negative = False
    if decimalNumber<0:
        negative = True
        decimalNumber *= -1
    hexList = []
    num = decimalNumber
    remainder = 0
    while num != 0:
        remainder = num % 16
        num = num - (int(remainder) / 16)
        num = int(num / 16)
        remainder = switchDecToHex(remainder)
        hexList.append(str(remainder))
    
    if negative:
        hexList.append('-')
    hexList.reverse()
    string = ""
    return string.join(hexList)

def hexToDec(hexadecimalNumber):
    hexList = list(hexadecimalNumber)
    hexList.reverse()
    negative = False
    if hexList[len(hexList)-1] == '-':
        negative = True
        hexList.pop()
    
    result = 0
    for i in range(len(hexList)-1, -1, -1):
        digitValue = int(switchHexToDec(hexList[i]))
        result = result + digitValue*(16**i)
    if negative:
        result *= -1
    return result

def binToHex(binaryNumber):
    #use the first 4 digits of binary number to get a hex digit
    negative = False
    if binaryNumber<0:
        negative = True
        binaryNumber *= -1
    binaryList = [int(x) for x in str(binaryNumber)]
    binaryList.reverse()
    hexList = []
    
    for i in range(0, len(binaryList), 4):
        temp = 0
        for j in range(4):
            if i+j <= len(binaryList)-1:
                temp = temp + (binaryList[i+j] * (2**j))
        hexNum = switchDecToHex(temp)
        hexList.append(str(hexNum))
    if negative:
        hexList.append('-')
    hexList.reverse()
    string = ''
    return string.join(hexList)
    
def hexToBin(hexadecimalNumber):
    hexList = list(hexadecimalNumber)
    hexList.reverse()
    binList = []
    negative = False
    if hexList[len(hexList)-1] == '-':
        negative = True
        hexList.pop()
    for i in range(len(hexList)):
        digit = int(switchHexToDec(hexList[i]))
        digitBinArray = ['0','0','0','0']
        for j in range(3,-1, -1):
            if int(digit) >= 2**j:
                digit = digit - 2**j
                digitBinArray[j] = '1'
        binList.extend(digitBinArray)
    binList.reverse()
    binaryString = ""
    binaryNumber = int(binaryString.join(binList))
    if negative:
        binaryNumber *= -1
    return binaryNumber
    
def decToFpn(decimalNumber):
    if decimalNumber<0:
        fpn = "1 "
        decimalNumber *= -1
    else:
        fpn = "0 "
    binary = decToBin(decimalNumber)
    binList = [int(x) for x in str(binary)]
    unbiasedExponent = len(binList)-1
    biasedExponent = 127 + unbiasedExponent
    unsignedBinary = decToBin(biasedExponent)
    fpn += str(unsignedBinary) + " "
    binary = int(str(binary)[0 : 0 : ] + str(binary)[0 + 1 : :])
    fpn += str(binary)
    for i in range(32 -len(fpn)):
        fpn += "0"
    return fpn

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

def format(string, string2):
    format = '{:>30}'
    format2 = '{:30}'
    string = string + "\t"
    formatted = format.format(string)
    formatted2 = format2.format(string2)
    formatFinal = formatted + formatted2
    return formatFinal


centerOne = 50
centerTwo = 80
number = -2045
binNumber = decToBin(number)
decimalNumber = binToDec(binNumber)
hexadecimalNumber = decToHex(decimalNumber)
decimalNumberFromHex = hexToDec(hexadecimalNumber)
hexadecimalNumberFromBinary = binToHex(binNumber)
binNumFromHex = hexToBin(hexadecimalNumber)
fpnFromDec = decToFpn(number)
decFromFpn = fpnToDec(fpnFromDec)

print(format("regular numb:" , str(number)))
print(format("bin from dec:" , str(binNumber)))
print(format("dec from bin:" , str(decimalNumber)))
print(format("hex from dec:" , str(hexadecimalNumber)))
print(format("dec from hex:" , str(decimalNumberFromHex)))
print(format("hex from bin:" , str(hexadecimalNumberFromBinary)))
print(format("bin from hex:", str(binNumFromHex)))
print(format("fpn from dec:", str(fpnFromDec)))
print(format("dec from fpn:", str(decFromFpn)))
