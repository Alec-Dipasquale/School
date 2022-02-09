
binary_numA = input("Enter number in Binary Format: ")
decimal_numA = int(binary_numA, 2)

binary_numB = input("Enter number that you want to subtract from the first number you entered - also in Binary Format: ")
decimal_numB = int(binary_numB, 2)

print(str(binary_numA)+"\t"+str(decimal_numA))
print("-" + str(binary_numB)+"\t-"+str(decimal_numB))

Result = decimal_numA - decimal_numB

binary_numC = bin(Result)[2:]

print (str(binary_numC) + "\t" + str(Result))