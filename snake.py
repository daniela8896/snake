from sqlite3 import Time
from turtle import *
import time


#creacion del cuerpo de la serpiente
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = [] #atributo
        self.create_snake() #metodo
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("violet")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)
        
    def move(self):
        #movimiento de la serpiente
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
    

        self.head.forward(20)
        
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

