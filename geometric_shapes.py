from turtle import Turtle, Screen
from helpers import colors
import random

screen = Screen()
tim = Turtle()

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for shape_sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides)


screen.exitonclick()