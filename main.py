from turtle import Turtle, Screen
import time

# Variables
snake = []
game_is_on = True

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

# Body snake
for index in range(3):
    snake.append(Turtle("square"))
    snake[index].penup()
    snake[index].color("white")

for index in range(1, len(snake)):
    snake[index].setx(snake[index - 1].xcor() - 20)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for index in range(len(snake) -1, 0, -1):
        print(index)
        print(snake[index].position())
        new_x = snake[index - 1].xcor()
        new_y = snake[index - 1].ycor()
        snake[index].goto(new_x, new_y)
    snake[0].forward(20)



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










# Screnn
screen.exitonclick()
