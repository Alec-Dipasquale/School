distance = 1
n = 10
sum=1
i = distance + 1
while ( i < n ):
    sum += i
    i += distance
    print("sum: " +str(sum) + "\t\ti: " + str(i))


print("\n Final Sum: " + str(sum))