year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day = int(input("Enter the day of the month: 1-31: "))
if month == 1 or month == 2:
    month += 12
    year -= 1
j = int(year // 100)
k = year % 100
dayOfWeek = ''
h = (day + 26 * (month+1)//10 + k + k//4 +j//4 +5*j) % 7

if h == 0:
    dayOfWeek += "Saturday"
elif h == 1:
    dayOfWeek += "Sunday"
elif h == 2:
    dayOfWeek += "Monday"
elif h == 3:
    dayOfWeek += "Tuesday"
elif h == 4:
    dayOfWeek += "Wednesday"
elif h == 5:
    dayOfWeek += "Thursday"
elif h == 6:
    dayOfWeek += "Friday"
print("Day of the week is " + dayOfWeek)