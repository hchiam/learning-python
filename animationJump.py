import turtle

# initialize
level = 1
x = 0
y = 0
scale = 50

# define a function to draw a line segment:
def drawLine(x,y,rotation,width,length):
    turtle.penup()
    turtle.goto(x,y)
    turtle.width(width)
    turtle.setheading(rotation)
    turtle.pendown()
    turtle.forward(length)
    return turtle.position()

#turtle.hideturtle()
turtle.dot(10)
turtle.speed(0) # this makes it go at full speed
turtle.goto(x,y) # go to starting position

time = [1.0*i/100.0 for i in range(0, 100)]

turtle.pencolor("black")

turtle.penup()
for t in time:
    f = 1 - (t*2-1)**2
    turtle.goto(t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t*2-1)**2 + t
    turtle.goto(t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t*2-1)**2 + t*2
    turtle.goto(t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

time = [2.0*i/100.0 for i in range(0, 100)]

turtle.pencolor("red")

turtle.penup()
for t in time:
    f = 1 - (t-1)**2
    turtle.goto(t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t-1)**2 + t/2
    turtle.goto(t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t-1)**2 + t
    turtle.goto(t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

time = [2.0*i/100.0 for i in range(0, 100)]

turtle.pencolor("blue")

turtle.penup()
for t in time:
    f = 1 - (t-1)**2
    turtle.goto(x,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t-1)**2 + t/2
    turtle.goto(x,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t-1)**2 + t
    turtle.goto(x,f*scale)
    turtle.pendown()
turtle.dot(10)

time = [1.0*i/100.0 for i in range(0, 100)]

turtle.pencolor("black")

turtle.penup()
for t in time:
    f = 1 - (t*2-1)**2
    turtle.goto(-t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t*2-1)**2 + t
    turtle.goto(-t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t*2-1)**2 + t*2
    turtle.goto(-t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

time = [2.0*i/100.0 for i in range(0, 100)]

turtle.pencolor("red")

turtle.penup()
for t in time:
    f = 1 - (t-1)**2
    turtle.goto(-t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t-1)**2 + t/2
    turtle.goto(-t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)

turtle.penup()
for t in time:
    f = 1 - (t-1)**2 + t
    turtle.goto(-t*scale,f*scale)
    turtle.pendown()
turtle.dot(10)


print("Drawing complete!")
print("--> Click on the new window to close it. <--")
turtle.exitonclick() # --> this prevents the "canvas" from disappearing immediately after the turtle draws it
print("Program finished! :)")