import random

def generateDNA(characters):
    s = ''
    dna = ["A", "G", "C", "T"]
    for i in range(0, characters):
        s += (random.choice(dna))
    return s



randomDNA = "B"
temp = randomDNA
count = 0
while not ("AGTC" in randomDNA):
    randomDNA = generateDNA(10000)
    print("NOPE")

temp = randomDNA
trimmedCount= 0
while True:
    if "AGTC" in temp:
        i = temp.find("AGTC")
        print(str(temp[i: i + 4]) + "\tCount: " + str(count))
        print( "Found at index: " + str(trimmedCount + i) + ", " + str(trimmedCount + i + 1) + ", " + str(trimmedCount + i + 2) + ", " + str(trimmedCount + i + 3))
        temp = temp[randomDNA.find("AGTC") + 3:]
        trimmedCount += i
        count += 1
    else:
        break
    