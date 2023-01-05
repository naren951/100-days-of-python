from turtle import Turtle

MOVE_DISTANCE = 10
TB_EDGE = 280
LR_EDGE = 380


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.xdirection, self.ydirection = -1,1
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.color("white")
        self.speed("fastest")
    
    def move(self):
        
        x,y = self.xcor(), self.ycor()        
        if y > TB_EDGE or y < -TB_EDGE:
            self.ydirection *= -1
         
        self.goto(x+self.xdirection*MOVE_DISTANCE,y+self.ydirection*MOVE_DISTANCE)
    
    def reset_ball(self):
        self.goto(0,0)
        self.xdirection, self.ydirection = -1,1