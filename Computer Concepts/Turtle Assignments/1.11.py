

population = 312032486
secPerYear = 365 * 24 * 60 * 60
birthsPer = secPerYear/7
deathsPer = secPerYear/13
immigrantsPer = secPerYear/45
yearlyGrowth = birthsPer + deathsPer + immigrantsPer


for i in range(5):
    population = population + yearlyGrowth
    print(int(population))
