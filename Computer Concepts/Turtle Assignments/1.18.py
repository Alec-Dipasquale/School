import turtle  

distance = 500
lineLength = distance*2

turtle.penup()
turtle.goto(0, distance)
turtle.pendown()
turtle.right(72)
for i in range(5):
    turtle.forward(lineLength)
    turtle.right(144)
    
turtle.done()