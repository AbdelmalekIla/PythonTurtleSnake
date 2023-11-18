from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\PC\OneDrive\Bureau\BootCamp 100 Day\day21\new_fille.txt", mode='r') as file:
            self.hiegh_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, max score :{self.hiegh_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hiegh_score:
            self.hiegh_score=self.score
            with open(r"C:\Users\PC\OneDrive\Bureau\BootCamp 100 Day\day21\new_fille.txt", mode='w') as file2:
                self.hiegh_score = file2.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
