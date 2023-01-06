import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.up,"Up")


game_is_on = True
i=0
while game_is_on:
    time.sleep(0.1*0.9**(scoreboard.level-1))
    screen.update()
    if i%6==0:
        car_manager.new_cars()
    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
    car_manager.move_cars()
    if player.finish_line_reached():
        scoreboard.increase_score()
    i+=1

screen.exitonclick()