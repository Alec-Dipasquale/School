import turtle  

x = [40, -40, -80, -40, 40, 80, 40]
y = [-69.28, -69.28, -9.8, 69, 69, 0, -69.28]
turtle.penup()
turtle.goto(x[0], y[0])
turtle.pendown()
for i in range(1, 7):
    turtle.goto(x[i], y[i])
    
turtle.done()