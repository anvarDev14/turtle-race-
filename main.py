from turtle import Screen
from car_manager import CarManager
from player import Player
import time
from scoreboard import Scoreboard


screen=Screen()
screen.title("Turtle race ")
screen.bgcolor("white")
screen.setup(600,600)
screen.tracer(0)
screen.listen()



car_manager=CarManager()
player=Player()
score=Scoreboard()

screen.onkeypress(player.go_up,"w")
screen.onkeypress(player.go_down,"s")






game_is_on=True
score.level2()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()







    for car in car_manager.all_cars :
        if player.distance(car)<25:
            score.game_over()
            game_is_on = False
            continue


    if player.ycor() > 280:
        car_manager.update_level()
        score.level2()
        player.goto(0,-280)
    if player.ycor()<-280:
        player.go_down()
        score.down()
        break
    if score.level==5:
        score.winner()
        break




















screen.exitonclick()
