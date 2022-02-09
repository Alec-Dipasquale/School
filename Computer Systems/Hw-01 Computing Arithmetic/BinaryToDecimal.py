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

num = 1011010
print("\n\nNumber: " + str(num))
print("Result: " + str(binToDec(num)) + "\n\n")