import random
dna = ["A", "G", "C", "T"]
random_sequence = ''
random_sequence2 = ''
isCompliment = True
count = 0
isAT = False
isTA = False
isCG = False
isGC = False

for i in range(0, 4):
    random_sequence += (random.choice(dna))

while True:
    count += 1
    random_sequence2 = ''
    for i in range(0, 4):
        random_sequence2 += (random.choice(dna))
    for i in range(0, len(random_sequence2)):
        isAT = (random_sequence[i] == 'A' and random_sequence2[i] == 'T')
        isTA = (random_sequence[i] == 'T' and random_sequence2[i] == 'A')
        isCG = (random_sequence[i] == 'C' and random_sequence2[i] == 'G')
        isGC = (random_sequence[i] == 'G' and random_sequence2[i] == 'C')

        if isAT or isTA or isGC or isCG:
            isCompliment = True
        else:
            isCompliment = False
            break


        

    if isCompliment:
        break
print(random_sequence)
print(random_sequence2)
print(count)