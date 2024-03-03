from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt","w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score_board()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
