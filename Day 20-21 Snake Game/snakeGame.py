import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = Scoreboard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increaseScore()
        scoreBoard.scoreCard()
    
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreBoard.game_over()
        time.sleep(3)
        scoreBoard.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.game_over()
            time.sleep(3)
            scoreBoard.reset()
            snake.reset()
screen.exitonclick()