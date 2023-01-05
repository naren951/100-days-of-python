from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 50, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.scoreCard()
    
    def scoreCard(self):
        self.speed("fastest")
        self.goto(0,200)
        self.hideturtle()
        self.clear()
        self.color("white")
        self.write(f"{self.l_score}           {self.r_score}",move=False,align=ALIGNMENT,font=FONT)
    
    def increase_l_score(self):
        self.l_score += 1
        self.reset()
        self.scoreCard()

    def increase_r_score(self):
        self.r_score += 1
        self.reset()
        self.scoreCard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align=ALIGNMENT,font=FONT)