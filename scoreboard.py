from turtle import Turtle


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.current_score = 0
        self.goto(0, -300)

    def you_lost(self):
        self.write("YOU LOST", False, "Center", ("Times New Roman", 80, "bold"))

    def you_won(self):
        self.write("YOU WON", False, "Center", ("Times New Roman", 80, "bold"))
