
x1 = float(input("Enter the x-coordinate for point 1: "))
y1 = float(input("Enter the y-coordinate for point 1: "))
x2 = float(input("Enter the x-coordinate for point 2: "))
y2 = float(input("Enter the y-coordinate for point 2: "))

slope = ( y2 - y1 ) / ( x2 - x1 )
string = "The slope for the line that connects two points (" + str(x1) + ", " + str(y1) + ") and (" + str(x2) + ', ' + str(y2) + ") is " + str(slope)
print(string)