import turtle
from turtle import Turtle, Screen
from helpers import random_color
import random

turtle.colormode(255)
screen = Screen()

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