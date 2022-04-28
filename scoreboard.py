from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 25, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 #atributo
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.write(f"El puntaje es: {self.score}", font=FONT, align=ALIGN)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Juego terminado! :( ", font=FONT, align=ALIGN)
