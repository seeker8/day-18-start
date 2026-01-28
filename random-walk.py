from turtle import Turtle, Screen
from data import colors
import random

screen = Screen()

tim = Turtle()
tim.shape('circle')
tim.width(6)
tim.speed(5)

width = screen.window_width() // 2
height = screen.window_height() // 2

for _ in range(50):
    tim.color(random.choice(colors))
    tim.setx(random.randint(-width, width))
    tim.sety(random.randint(-height, height))


screen.exitonclick()