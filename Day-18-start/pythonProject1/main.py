import random
import turtle
from turtle import *


tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.pensize(1)
tim.speed(0)

def draw_spirograpg(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_gap)
        tim.circle(100)

draw_spirograpg(5)

screen = Screen()
screen.exitonclick()