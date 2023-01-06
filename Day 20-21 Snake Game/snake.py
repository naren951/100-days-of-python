from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):    
        init = 0
        for _ in range(3):
            self.add_segment((init,0))
            init-=20
        
    def add_segment(self,position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment((self.segments[-1].xcor(),self.segments[-1].ycor()))

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].xcor(),self.segments[i-1].ycor())
        self.head.forward(MOVE_DISTANCE)
    
    def reset(self):
        for seg in self.segments:
            seg.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN: 
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)