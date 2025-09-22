import turtle
import math

def hearta(k):
    return 12*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed("fastest")
bgcolor("black")
for i in range(1000):
    goto(hearta(i)*20, heartb(i)*20)
    color("red")
    dot(1)
done()
