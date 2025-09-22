# heart.py
# Draws a layered red heart pattern and writes "I love you for ever" in the center.
# Save as heart.py and run with: python heart.py

import turtle
import math
import time

# --- Setup screen ---
screen = turtle.Screen()
screen.title("Heart — I love you for ever")
screen.bgcolor("black")
screen.setup(width=800, height=700)  # window size
screen.tracer(False)  # turn off automatic drawing for faster animation

# --- Pen for drawing the heart pattern ---
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
pen.color("red")
pen.penup()

# Parametric heart curve (famous heart curve)
def heart_point(t):
    # t in radians
    x = 16 * math.sin(t) ** 3
    y = (13 * math.cos(t)
         - 5 * math.cos(2 * t)
         - 2 * math.cos(3 * t)
         - math.cos(4 * t))
    return x, y

# Scale and center transform (so it fits nicely)
SCALE = 12
OFFSET_X = 0
OFFSET_Y = -20

# Draw multiple shifted/rotated copies to create the layered effect
copies = 14            # how many overlapping heart outlines
angle_step = 6         # degrees of rotation between each copy

for copy_index in range(copies):
    rot_deg = copy_index * angle_step
    rot_rad = math.radians(rot_deg)

    # Move to first point without drawing
    t0 = 0.0
    x0, y0 = heart_point(t0)
    # apply rotation and scaling
    xr = x0 * math.cos(rot_rad) - y0 * math.sin(rot_rad)
    yr = x0 * math.sin(rot_rad) + y0 * math.cos(rot_rad)
    pen.goto(xr * SCALE + OFFSET_X, yr * SCALE + OFFSET_Y)
    pen.pendown()

    # Draw the heart parametric curve
    steps = 200
    for i in range(1, steps + 1):
        t = (i / steps) * 2 * math.pi
        x, y = heart_point(t)
        xr = x * math.cos(rot_rad) - y * math.sin(rot_rad)
        yr = x * math.sin(rot_rad) + y * math.cos(rot_rad)
        pen.goto(xr * SCALE + OFFSET_X, yr * SCALE + OFFSET_Y)

    pen.penup()

    # tiny refresh after each copy so you see the layering build up
    if copy_index % 2 == 0:
        screen.update()
        # slight pause for animation effect (remove or decrease for speed)
        time.sleep(0.05)

# final update to show completed pattern
screen.update()

# --- Center text ---
text_writer = turtle.Turtle()
text_writer.hideturtle()
text_writer.penup()
text_writer.goto(0, -10)   # center-ish; adjust y to taste
text_writer.color("white")
text_writer.write("I love you for ever", align="center", font=("Arial", 24, "bold"))

# keep window open until closed by user
screen.tracer(True)
turtle.done()
