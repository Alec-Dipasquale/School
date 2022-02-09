

month_name = int(input("Enter a month in the year(e.g., 1 for Jan): "))
year = int(input("Enter a year: "))

if month_name == 2:
    if year % 4 == 0:
        print("February " + str(year) + "has 28 days")
    else:
        print("February " + str(year) + " has 28 days")
elif month_name == 4:
    print("April " + str(year) +" has 30 days")
elif month_name == 6:
    print("June " + str(year) +" has 30 days")
elif month_name == 9:
    print("September " + str(year) +" has 30 days")
elif month_name ==11:
    print("November " + str(year) +" has 30 days")
elif month_name == (1):
    print("January " + str(year) +" has 31 day")
elif month_name == (3):
    print("March " + str(year) +" has 31 day")
elif month_name == (5):
    print("May " + str(year) +" has 31 day")
elif month_name == (7):
    print("July " + str(year) +" has 31 day")
elif month_name == (8):
    print("August " + str(year) +" has 31 day")
elif month_name == (10):
    print("October " + str(year) +" has 31 day")
elif month_name == (12):
    print("December " + str(year) +" has 31 day")
else:
    print("Wrong month number")