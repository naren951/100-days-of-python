from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y = -80
for i in colors:
    tim = Turtle(shape="turtle")
    tim.color(i)
    tim.penup()
    tim.goto(-230,y)
    y+=25
    turtles.append(tim)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if bet == turtle.pencolor():
                print(f"You've Won! The {turtle.pencolor()} turtle is the winner.")
            else:
                print(f"You've Lost! The {turtle.pencolor()} turtle is the winner.")

    for turtle in turtles:
        turtle.forward(random.randint(0,10))





screen.exitonclick()
