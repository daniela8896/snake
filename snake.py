from sqlite3 import Time
from turtle import *
import time

# crear escenario
screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

screen.tracer(0)

#creacion del cuerpo de la serpiente
starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    snake_segment = Turtle("square")
    snake_segment.color("violet")
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment)
    

'''
snake_segment = Turtle("square")
snake_segment.color("white")

snake_segment = Turtle("square")
snake_segment.color("white")
snake_segment.goto(-20, 0)

snake_segment = Turtle("square")
snake_segment.color("white")
snake_segment.goto(-40, 0)
'''

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    # for segment in segments:
    #     segment.forward(20)
    #     segment[0].left(90)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
  

    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()