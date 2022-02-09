import turtle 


distance = 50
lineLength = 100
turtle.penup()
turtle.goto(0, distance)
turtle.pendown()
turtle.right(120)
for i in range(3):
    turtle.forward(lineLength)
    turtle.left(120)

turtle.done()