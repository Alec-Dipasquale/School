import turtle

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
lineLength = 100
for i in range(4):
    for i in range(4):
        turtle.forward(lineLength)
        turtle.right(90)
    turtle.left(90)
turtle.done()