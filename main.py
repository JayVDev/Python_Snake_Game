from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Variables
game_is_on = True

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create a snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Screen listen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
# Body snake
# for _ in range(2):
#     new_snake = Turtle()
#     new_snake.color("white")
#     new_snake.shape("square")
#     snake.append(new_snake)
#
# snake[1].setx(-20)
#
# for index in range(0, len(snake)):
#     snake[index].penup()
#     print(f"index : {index} : position: {snake[index].xcor()}")
#     snake[index].setx(snake[index].xcor() + 20)
#
#
# for index in range(0, len(snake)):
#     print(f"index : {index} : position: {snake[index].xcor()}")

# snake_01 = Turtle()
# snake_02 = Turtle()
# snake_03 = Turtle()
#
# snake_01.color("red")
# snake_02.color("white")
# snake_03.color("orange")
#
#
# snake_01.shape("square")
# snake_02.shape("square")
# snake_03.shape("square")
#
# snake_01.setx(0)
# snake_02.setx(-20)
# snake_03.setx(-40)
# Screen

screen.exitonclick()
