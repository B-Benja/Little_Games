from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Cross the road")
# for random RGB colors
screen.colormode(255)

player = Player()
car = Cars()
scoreboard = Score()

print(car)


screen.listen()
screen.onkey(player.player_move_forward, "Up")
screen.onkey(player.player_move_backward, "Down")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.random_spawn()
    car.move_forward()

    if player.ycor() > 280:
        scoreboard.winning()
        car.level_up()
        player.player_reset()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            player.player_reset()
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
