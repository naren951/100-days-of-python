import time
from turtle import Screen
from ball import Ball
from paddle import Paddle

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreBoard = Scoreboard()
r_paddle = Paddle((400,0))
l_paddle = Paddle((-400,0))
ball = Ball()


screen.listen()

screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if l_paddle.distance(ball) < 45 and ball.xcor() > -440 or r_paddle.distance(ball) < 45 and ball.xcor() < 440:
        ball.xdirection*=-1
        ball.move_speed*=0.9
    
    if ball.xcor() > 430:
        ball.reset_ball()
        scoreBoard.increase_l_score()
    elif ball.xcor() < -430: 
        scoreBoard.increase_r_score()
        ball.reset_ball()
        ball.move_speed = 0.1

screen.exitonclick()