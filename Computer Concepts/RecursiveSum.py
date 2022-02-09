import sys

sys.setrecursionlimit(10**6) 

def recursiveSum(x):
    if  x >1:
        return recursiveSum(x-1) + x
    else:
        return 1

userInput = input("Enter a number to sum: ")

print("the recursive sum is " + str(recursiveSum(int(userInput))))

"""
2. Yes there is a regularity in the sums. They all seem
to contain two 5s. The bigger the number the more 0s follow
each of the 5s.
"""

n = int(input("Enter the value of n for efficient sum: "))

sum = int(n * (n+1)/2)

print("sum = " + str(sum))