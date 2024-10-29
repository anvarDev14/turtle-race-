from turtle import Turtle
import random

from scoreboard import Scoreboard


COLORS=["red","blue","yellow","purple","green"]

STARTING_MOVE_SPEED=5
score=Scoreboard

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_sped=STARTING_MOVE_SPEED

    def create_cars(self):
        random_chanse = random.randint(1, 6)
        if random_chanse == 1:
            new_car=Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_sped)



    def update_level(self):
        self.car_sped+=5


