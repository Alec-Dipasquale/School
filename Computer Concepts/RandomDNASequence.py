import random
dna = ["A", "G", "C", "T"]
random_sequence = ''

for i in range(0, 8):
    random_sequence += (random.choice(dna) + " ")
print(random_sequence)