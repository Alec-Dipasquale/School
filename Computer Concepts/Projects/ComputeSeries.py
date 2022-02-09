
def m(x):
    sum = 0
    for i in range(1, x + 1):
        sum += (i / (i+1))
    return sum
        
x = 10

print ("i\tm(i)")
for k in range(1, x + 1):
    print(str(k) + "\t%0.4f" % m(k))