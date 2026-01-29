from turtle import Turtle
ALIGN = "center"
FONT = ("Roboto", 24, "normal")


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()
        #self.high_score = self.get_high_score()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()