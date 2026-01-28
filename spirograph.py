import turtle
from turtle import Turtle, Screen
from helpers import random_color

turtle.colormode(255)
screen = Screen()
jiji = Turtle()
jiji.speed('fastest')

angle = 0
while angle < 360:
    jiji.pencolor(random_color())
    jiji.circle(100)
    angle += 5
    jiji.setheading(angle)



screen.exitonclick()
