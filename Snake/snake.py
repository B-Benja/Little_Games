from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# create snake body
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        # define the head of the snake
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setposition(position)
        self.snake_body.append(snake)

    def extend(self):
        # extend a new segment to the snake body
        self.add_snake(self.snake_body[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[seg_num].goto(self.snake_body[seg_num - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        # to remove the old snake form screen
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]