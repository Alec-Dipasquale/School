#To convert digit to letter in hex
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

#To convert a letter to its equivelent number in hex
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

#convert a given binary number to hexadecimal string
def binToHex(binaryNumber):
    #Check if negative and store for end
    negative = False
    if binaryNumber<0:
        negative = True
        binaryNumber *= -1
    binaryList = [int(x) for x in str(binaryNumber)]
    binaryList.reverse()
    hexList = []
    #goes through 4 binary numbers at a time 
    #and converts it to a single hex digit
    for i in range(0, len(binaryList), 4):
        temp = 0
        for j in range(4):
            if i+j <= len(binaryList)-1:
                temp = temp + (binaryList[i+j] * (2**j))
        hexNum = switchDecToHex(temp)
        hexList.append(str(hexNum))
    #turns it back negative
    if negative:
        hexList.append('-')
    hexList.reverse()
    string = ''
    return string.join(hexList)
    
#convert a hexidecimal string to a binary integer
def hexToBin(hexadecimalNumber):
    hexList = list(hexadecimalNumber)
    hexList.reverse()
    binList = []
    negative = False
    #check for negative and store for end
    if hexList[len(hexList)-1] == '-':
        negative = True
        hexList.pop()
    #takes a single hex digit at a time and loops 4 times
    #over it to get the highest to lowest 4 binary digits
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
    #check for negative and store for end
    if negative:
        binaryNumber *= -1
    return binaryNumber

hexadecimal = binToHex(-100011101)
print("Binary to Hex: " + hexadecimal)
print("Hexadecimal to Binary: " + str(hexToBin(hexadecimal)))