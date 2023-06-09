from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.score += 1
        snake.extend()
        scoreboard.refresh_score()

    if snake.head.xcor() > 289 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -285:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()

# for square_num in range(start=2, stop=0, step=-1):  # This range func comes from C language won't work in python
