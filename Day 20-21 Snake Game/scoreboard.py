from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt",mode='r') as file:
            try:            
                self.high_score = int(file.read())
            except:
                self.high_score = 0
        self.scoreCard()
    
    def scoreCard(self):
        self.speed("fastest")
        self.goto(0,250)
        self.hideturtle()
        self.clear()
        self.color("white")
        self.write(f"Score = {self.score} High Score = {self.high_score}",move=False,align=ALIGNMENT,font=FONT)
    
    def increaseScore(self):
        self.score += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt",mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.scoreCard()