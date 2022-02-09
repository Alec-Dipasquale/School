'''
(Financial application: compute the future investment value)

Write a function that computes a future investment value at a given interest rate for a 
specified number of years. The future investment is determined using the formula in Programming 
Exercise 2.19 in Chapter 2 Programming Exercise from the Book.

Use the following function header:

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):

For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.

Write a test program that prompts the user to enter the investment amount and the annual 
interest rate in percent and prints a table that displays the future value for the years from 
1 to 30.
Sample Run

The amount invested: 1000

Annual interest rate: 9

Years Future Value

1 1093.80

2 1196.41

...

29 13467.25

30 14730.58
'''

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    accumulatedValue = investmentAmount * (( 1 + monthlyInterestRate)**(years*12))
    return round(accumulatedValue, 2)

investedAmount = int(input("The amount invested: "))
interestRate = int(input("Annual interest rate: "))
monthlyInterestRate = (interestRate)/1200

print("Years\tFuture\tValue")
for i in range(1, 31):
    print(str(i) + "\t" + str(futureInvestmentValue(investedAmount, monthlyInterestRate, i)))