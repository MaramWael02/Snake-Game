from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.speed = 20
        self.tail = self.snake_blocks[-1]
        self.head = self.snake_blocks[0]

    def create_snake(self):
        last_position = 0
        for _ in range(3):
            block = Turtle("square")
            block.goto((last_position, 0))
            block.color("white")
            block.penup()
            self.snake_blocks.append(block)
            last_position += 20
        self.head = self.snake_blocks[0]
        self.tail = self.snake_blocks[- 1]

    def move(self):
        for block_num in range(len(self.snake_blocks) - 1, 0, -1):
            x = self.snake_blocks[block_num - 1].xcor()
            y = self.snake_blocks[block_num - 1].ycor()
            self.snake_blocks[block_num].goto(x, y)
        self.snake_blocks[0].forward(25)

    def move_to_the_left(self):
        if self.snake_blocks[0].heading() != RIGHT:
            self.snake_blocks[0].setheading(LEFT)

    def move_to_the_right(self):
        if self.snake_blocks[0].heading() != LEFT:
            self.snake_blocks[0].setheading(RIGHT)

    def move_up(self):
        if self.snake_blocks[0].heading() != DOWN:
            self.snake_blocks[0].setheading(UP)

    def move_down(self):
        if self.snake_blocks[0].heading() != UP:
            self.snake_blocks[0].setheading(DOWN)

    def add_snake(self):
        block = Turtle("square")
        block.color("white")
        block.penup()
        pos_x = self.tail.xcor()
        pos_y = self.tail.ycor()
        if self.tail.heading() == UP:
            pos_y -= 20
        elif self.tail.heading() == DOWN:
            pos_y += 20
        elif self.tail.heading() == RIGHT:
            pos_x -= 20
        else:
            pos_x += 20
        block.goto(pos_x, pos_y)
        self.snake_blocks.append(block)
        self.move()
