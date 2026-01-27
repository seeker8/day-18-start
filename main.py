from turtle import Turtle, Screen

jiji = Turtle()
jiji.shape("turtle")
jiji.color("DodgerBlue")
jiji.turtlesize(2, 2)

for i in range(4):
    jiji.forward(100)
    jiji.right(90)
screen = Screen()
screen.exitonclick()