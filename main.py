from turtle import Turtle, Screen

jiji = Turtle()
jiji.shape("turtle")
jiji.color("DodgerBlue")
jiji.turtlesize(2, 2)
jiji.pensize(2)


screen = Screen()
# draw a square
# for i in range(4):
#     jiji.forward(100)
#     jiji.right(90)


# move the starting point
    # jiji.penup()
    # jiji.setx(-500)
    # jiji.pendown()
# draw a dashed line 10x
# draw a gap 10x
# draw a solid line 10x
for i in range(4):
    for _ in range(20):
        jiji.forward(5)
        if jiji.isdown():
            jiji.penup()
        else:
            jiji.pendown()
    jiji.penup()
    jiji.forward(100)
    jiji.pendown()
    jiji.forward(100)
    jiji.right(90)


screen.exitonclick()