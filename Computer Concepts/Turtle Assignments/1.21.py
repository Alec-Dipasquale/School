import turtle  

size = 300
partOfSize = (size/2)
mostOfSize =(size/10)

turtle.speed(0)
turtle.penup()
turtle.goto(0, -size)
turtle.pendown()
turtle.circle(size)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.seth(0)
for i in range(4):
    if i  == 1:
        turtle.penup()
    turtle.forward(partOfSize)
    turtle.penup()
    turtle.forward(partOfSize-mostOfSize)
    turtle.write(3 * (i +1))
    if i == 1:
        turtle.forward(mostOfSize*2)
        turtle.write("9:15:00")
        turtle.back(mostOfSize*2)
    turtle.back(partOfSize-mostOfSize)
    turtle.back(partOfSize)
    turtle.pendown()
    turtle.right(90)

turtle.done()