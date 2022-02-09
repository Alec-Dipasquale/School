#Alec Dipasquale
#Chapter 2: Programming Project 5

investmentAmount = float(input("Enter investment amount: ") )
annualInterestRate = float(input("Enter annual interest rate: "))
numOfYears = float(input("Enter number of years: "))
monthlyInterestRate = annualInterestRate/1200
accumulatedValue = investmentAmount * (( 1 + monthlyInterestRate)**12)

print("Accumulated value is " + str(round(accumulatedValue, 2)))
