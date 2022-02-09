import turtle  

def side():
    heading = turtle.heading()
    turtle.seth(0)
    turtle.left(30)
    turtle.forward(l)
    turtle.back(l)
    return heading

turtle.speed(0)
l = 1
w = 2
h = 1
size = 100
l *= size
w *= size
h *= size
turtle.penup()
turtle.goto(-size/2, -size/2)
turtle.pendown()


for i in range(1, 5):
    if i % 2 == 0:
        turtle.forward(h)
        turtle.left(side())
        turtle.left(60)
    else :
        turtle.forward(w)
        turtle.left(side())
        turtle.left(60)
turtle.left(30)
turtle.forward(l)
turtle.seth(0)
for i in range(1, 5):
    if i % 2 == 0:
        turtle.forward(h)
        turtle.left(90)
    else :
        turtle.forward(w)
        turtle.left(90)
    
turtle.done()