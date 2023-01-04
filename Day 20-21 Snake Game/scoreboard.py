from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.scoreCard()
    
    def scoreCard(self):
        self.speed("fastest")
        self.goto(0,250)
        self.hideturtle()
        self.clear()
        self.color("white")
        self.write(f"Score = {self.score}",move=False,align=ALIGNMENT,font=FONT)
    
    def increaseScore(self):
        self.score += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align=ALIGNMENT,font=FONT)