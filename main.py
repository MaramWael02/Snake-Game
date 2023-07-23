from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(key="Left", fun=snake.move_to_the_left)
my_screen.onkey(key="Right", fun=snake.move_to_the_right)
my_screen.onkey(key="Up", fun=snake.move_up)
my_screen.onkey(key="Down", fun=snake.move_down)

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_blocks[0].distance(food) < 25:
        food.move()
        scoreboard.increase_score()
        snake.add_snake()

    if snake.snake_blocks[0].xcor() > 280.0 or snake.snake_blocks[0].xcor() < -280.0 or \
            snake.snake_blocks[0].ycor() > 280.0 or snake.snake_blocks[0].ycor() < -280.0:
        scoreboard.gameover()
        game_is_on = False

    for block in snake.snake_blocks[2:]:
        if snake.snake_blocks[0].distance(block) < 5:
            scoreboard.gameover()
            game_is_on = False

my_screen.exitonclick()
