import turtle
from turtle import Turtle, Screen
from data import colors
import random

turtle.colormode(255)
screen = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tim = Turtle()
tim.shape('circle')
tim.pensize(6)
tim.speed(5)

width = screen.window_width() // 2
height = screen.window_height() // 2

for _ in range(50):
    tim.pencolor(random_color())
    tim.setx(random.randint(-width, width))
    tim.sety(random.randint(-height, height))


screen.exitonclick()