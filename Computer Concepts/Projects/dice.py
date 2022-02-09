
import random
#simulate rolling a pair of dice
count = 0
trials = 1000
for i in range(trials):
    die1 = random.randrange(6) + 1
    die2 = random.randrange(6) + 1
    if die1 + die2 == 7:
        print(str(die1) + " + " + str(die2) + " = 7")
        count += 1

probability = count / trials 
print(probability)