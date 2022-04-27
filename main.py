from turtle import Screen
from snake import Snake
from food import Food
import time

# crear escenario
screen = Screen()  # instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

screen.tracer(0)

#crear - instanciar el objeto serpiente
snake = Snake()

#instancio el objeto comida
food = Food()

#movimientos serpiente
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

screen.exitonclick()
