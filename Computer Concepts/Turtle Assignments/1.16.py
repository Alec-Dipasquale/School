import turtle

distance = 50
lineLength = 100
turtle.penup()
turtle.goto(distance, distance)
turtle.pendown()
turtle.circle(distance, extent=None, steps=None)

turtle.penup()
turtle.goto(-distance, -distance)
turtle.pendown()
turtle.circle(distance, extent=None, steps=None)

turtle.penup()
turtle.goto(distance, -distance)
turtle.pendown()
turtle.circle(distance, extent=None, steps=None)

turtle.penup()
turtle.goto(-distance, distance)
turtle.pendown()
turtle.circle(distance, extent=None, steps=None)

turtle.done()