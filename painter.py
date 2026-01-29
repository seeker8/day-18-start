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
x = -250
y = -250
jimi = Turtle()
jimi.hideturtle()
jimi.penup()
jimi.goto(x, y)
jimi.speed("fastest")
for z in range(10):
    jimi.goto(-250, y + (z * 50))
    for _ in range(10):
        jimi.dot(20, random.choice(rbg_colors))
        jimi.forward(50)


screen.exitonclick()