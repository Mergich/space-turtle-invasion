from turtle import Turtle


class Ammo(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=0.1)
        self.color("skyblue")
        self.pu()
        # self.x_move = 0
        self.y_move = 12
        self.move_speed = 0.01

    def shoot(self):
        # new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def reset_position(self, position_x, position_y):
        self.goto(position_x, position_y)
        self.move_speed = 0.01

    def enemy_shoot(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)

    def reset_enemy_shoot(self, position_x, position_y):
        self.goto(position_x, position_y)
        self.move_speed = 0.01
