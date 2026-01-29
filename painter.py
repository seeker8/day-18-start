# this code was used to generate the rgb color list in helpers
#import colorgram
# colors = colorgram.extract('spot.png', 30)
# normalized_colors = []
import turtle

# for color in colors:
#     r,g,b = color.rgb
#     normalized_colors.append((r,g,b))
#
# print(normalized_colors)

from helpers import rbg_colors
from turtle import Turtle, Screen
import random


# canvas 10 x 10 dots
# each dot should be size 20
# separated by 50
turtle.colormode(255)
screen = Screen()
jimi = Turtle()
jimi.speed("fastest")
for y in range(10):
    jimi.goto(0, y * 50)
    for _ in range(10):
        jimi.color(random.choice(rbg_colors))
        jimi.dot(20)
        jimi.penup()
        jimi.forward(50)


screen.exitonclick()