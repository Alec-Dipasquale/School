import turtle  


x, y, x2, y2 = -39, 48, 50, -50


turtle.penup()
turtle.goto(x, y)
turtle.write("(" + str(x) +',' + str(y) + ')')
turtle.pendown()
turtle.color("red")
turtle.goto(x2,y2)
turtle.color("black")
turtle.write("(" + str(x2) +',' + str(y2) + ')')

turtle.done()