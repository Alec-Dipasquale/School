number = float(input('Input a number: '))
iterations = 500
a = float(number) # number to get square root of
for i in range(iterations): # iteration number
    number = 0.5 * (number + a / number) # update

print('The square root of ' + str(a) + ' is ' + str(number))
