from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
TB_EDGE = 280
LR_EDGE = 420

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)
    
    def create_paddle(self,position):
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.seth(UP)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < TB_EDGE:
            self.seth(UP)
            self.forward(MOVE_DISTANCE)
    
    def down(self):
        if self.ycor() > -TB_EDGE:
            self.seth(DOWN)
            self.forward(MOVE_DISTANCE)