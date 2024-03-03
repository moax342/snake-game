from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen related variables
sc = Screen()
sc.title("Snake Game")
sc.bgcolor("Black")
sc.tracer(0)
sc.setup(height=600, width=600)
sc.listen()

# Main classes used in the game
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# the snake control
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")

game_is_over = True

while game_is_over:
    """Running the snake until the the game is over variable is set to False"""
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision to the Ball
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect the collision to the  Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect the collision to the snake body
    for segment in snake.snakebody[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

sc.exitonclick()
