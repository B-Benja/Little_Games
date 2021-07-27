from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        # to slow down the ball movement
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_direction(self):
        self.y_move *= -1

    def change_direction_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def next_round(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_move *= -1