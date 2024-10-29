from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.shapesize()
        self.setheading(90)
        self.penup()
        self.goto(0,-280)



    def go_up(self):
        y_cor=self.ycor()+20
        self.goto(self.xcor(),y_cor)



    def go_down(self):
        y_cor=self.ycor()-20
        self.goto(self.xcor(),y_cor)


