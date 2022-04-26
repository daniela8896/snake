from turtle import *

# crear escenario
screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

#creacion del cuerpo de la serpiente
positions = [(0,0), (-20, 0), (-40, 0)]

for position in positions:
    snake_segment = Turtle("square")
    snake_segment.color("violet")
    snake_segment.goto(position)

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



screen.exitonclick()