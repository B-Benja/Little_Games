from turtle import Turtle


FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.winning()

    def winning(self):
        self.clear()
        self.level += 1
        self.goto(-260, 240)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
