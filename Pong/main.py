from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# initialize paddles and ball
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
# left player
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
# right player
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction()

    # detect collision with paddle (right)
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or (ball.distance(paddle_left) < 50 and ball.xcor() < -320):
        ball.change_direction_paddle()

    # detect left paddle miss
    if ball.xcor() < -400:
        ball.next_round()
        score.right_point()

    # detect right paddle miss
    if ball.xcor() > 400:
        ball.next_round()
        score.left_point()

screen.exitonclick()