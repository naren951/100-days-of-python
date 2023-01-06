from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.scoreCard()

    def scoreCard(self):
        self.speed("fastest")
        self.goto(-250,250)
        self.hideturtle()
        self.clear()
        self.write(f"Level: {self.level}",font=FONT)
    
    def increase_score(self):
        self.level+=1
        self.scoreCard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align="center",font=FONT)