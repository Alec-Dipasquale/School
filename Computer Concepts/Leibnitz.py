iterations = int(input('Number of iterations: '))

pi = 1
num = 3
for i in range(1,iterations+1):
    if i % 2 == 0:
        pi = pi + (1/num)
    else:
        pi = pi - (1/num)
    num = num + 2
print(pi)