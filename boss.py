MOVE_DISTANCE = 50
from random import *

from turtle import Turtle


class Boss(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_wid=15, stretch_len=15)
        self.pu()
        self.goto(position)
        self.x_move = 1
        # self.y_move = 0
        self.move_speed = 0.01

    def shoot(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def enemy_move_right(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def enemy_move_left(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())

    def bounce(self):
        self.x_move *= -1