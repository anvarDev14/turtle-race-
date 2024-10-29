from turtle import Turtle
import car_manager



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.y_move = 10
        self.x_move = 10



    def level2(self):
        self.goto(-225,250)
        self.level+=1
        self.penup()
        self.clear()
        self.write(f"LEVEL {self.level}", align="center", font=("Arial", 24, "normal"))




    def add(self):
        self.level+=1
        car_manager.STARTING_MOVE_SPEED+=5
        self.clear()
        self.level2()

    def move(self):
        x_move=self.xcor()+self.x_move
        y_move=self.ycor()+self.y_move
        self.goto(x_move,y_move)

    def bounce_y(self):
        self.y_move*=-1


    def bounce_x(self):
        self.x_move*=-1



    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def winner(self):
        self.goto(0,0)
        self.penup()
        self.write(f"YOU WIN", align="center", font=("Arial", 24, "normal"))

    def down(self):

        self.penup()
        self.goto(0,0)
        self.write(f"PLEASE PRESS 'w' BUTTON ", align="center", font=("Arial", 24, "normal"))