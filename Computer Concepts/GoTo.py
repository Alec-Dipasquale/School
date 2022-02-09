import turtle
import random


turtle.speed(0)

def drawGraphWithInclines():
    incline = 250
    barLine = incline*2 
    turtle.pensize(3)
    turtle.goto(0,0)
    turtle.goto(0,barLine)
    turtle.goto(0,0)
    turtle.goto(barLine,0)
    turtle.goto(0,0)
    turtle.goto(incline,incline)
    turtle.goto(0,0)
    turtle.goto(incline,-incline)
    turtle.goto(0,0)
    turtle.goto(0,-barLine)
    turtle.goto(0,0)
    turtle.goto(-incline,-incline)
    turtle.goto(0,0)
    turtle.goto(-barLine, 0)
    turtle.goto(0,0)
    turtle.goto(-incline, incline)
    turtle.goto(0,0)

    turtle.done()

def designOne():
    i = 1
    while i != -99:
        if i % 20 == 0:
            turtle.left(30)
            turtle.forward(random.randint(0,3)*30)
            i = 1
            turtle.forward(i/2)
            turtle.right(60)
            turtle.forward(i/2)
            turtle.left(i/2)
        else:
            turtle.forward(i)
            turtle.right(60)
            turtle.forward(i)
            turtle.left(i)
            i += 1

designOne()