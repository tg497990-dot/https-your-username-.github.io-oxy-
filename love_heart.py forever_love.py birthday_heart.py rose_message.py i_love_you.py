import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Glowing Heart with Text")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")

# Function to draw a heart shape using parametric equations
def heart(t):
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x, y

# Draw multiple glowing lines
pen.hideturtle()
for k in range(40):   # number of layers
    pen.penup()
    for i in range(361):   # draw 0° to 360°
        t = math.radians(i)
        x, y = heart(t)
        x = x * 10   # scale heart
        y = y * 10
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x + k, y + k)  # offset to create glowing effect
    pen.penup()

# Write text in the center
pen.goto(0, -20)  # adjust position
pen.color("white")
pen.write("I LOVE YOU FOR EVER", align="center", font=("Arial", 18, "bold"))

turtle.done()
