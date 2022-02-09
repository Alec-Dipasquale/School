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

def binToHex(binaryNumber):
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
    hexList.reverse()
    string = ''
    return string.join(hexList)
    
binaryNumber = input("Enter a binary number: ")
print("The hex value is " + str(binToHex(binaryNumber)))