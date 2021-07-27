import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake, Snake, Snake")
screen.tracer(0)

# initialize Fod, Snake and Scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# use the arrow keys for navigation
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# move the snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # to detect the collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    # to detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        # game_on = False
        score.reset_game()
        snake.reset()

    # to detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            # game_on = False
            score.reset_game()
            snake.reset()


screen.exitonclick()
