x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

inRectangle = True

if x > 5 or x<-5 or y>5/2 or y<-5/2:
    print ("Point (" + str(x) + ',' + str(y) + ") is not in the rectangle")
else:
    print ("Point (" + str(x) + ',' + str(y) + ") is in the rectangle")
