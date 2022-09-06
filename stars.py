from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class StarManager:

    def __init__(self):
        # self.all_stars = []
        # self.star_speed = STARTING_MOVE_DISTANCE

    # def create_star(self):
        for i in range(2):
            new_star = Turtle("square")
            new_star.shapesize(stretch_wid=0.01, stretch_len=0.01)
            new_star.penup()
            new_star.color('white')
            random_y = random.randint(-450, 450)
            random_x = random.randint(-650, 650)
            new_star.goto(random_x, random_y)
            # self.all_stars.append(new_star)

    # def move_stars(self):
    #     for star in self.all_stars:
    #         star.backward(self.all_stars)