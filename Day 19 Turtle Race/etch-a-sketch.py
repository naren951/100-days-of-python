import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def turn_left():
    tim.seth(tim.heading() + 10)


def turn_right():
    tim.seth(tim.heading() - 10)

def clear_drawing():
    tim.clear()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
