
inputMinutes = int(input("Enter the number of minutes: "))
minPH = 60
hourPD = 24
dayPY = 365
inputDays = (inputMinutes/minPH)/hourPD
remainingDays = int(inputDays) % dayPY
inputDays -= remainingDays
inputYears = int(int(inputDays)/dayPY)

print(str(inputMinutes) + 'minutes is approximately ' + str(inputYears) + 
      ' years and ' + str(remainingDays) + ' days')