import turtle

k = turtle.Turtle()
k.resizemode("user")
k.shapesize(560 // (n*42), 560 // (n*42), outline=None)
for i in range(10):
    k.stamp()
    k.forward(10)
turtle.exitonclick()