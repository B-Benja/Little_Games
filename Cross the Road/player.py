from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player_reset()

    def player_move_forward(self):
        self.forward(20)

    def player_move_backward(self):
        self.backward(20)

    def player_reset(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)