import random
from turtle import Turtle
from turtle import Screen
from starship import StarShip
from ammo import Ammo
import time
from boss import Boss

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1300, height=900)
screen.title("Space Turtle Invasion")
screen.tracer(0)

boss = Boss((100, 280))
boss.shapesize(stretch_wid=15, stretch_len=15)
boss.color('white')
boss.shape('turtle')
boss.right(90)

boss_ammo_one = Ammo()
boss_ammo_two = Ammo()
boss_ammo_three = Ammo()
boss_ammo_four = Ammo()
boss_ammo_five = Ammo()
boss_ammo_six = Ammo()

starship_1 = StarShip((0, -360))
# ------------------------------------------------THE FIRST WING--------------------------------------------------------

starship_2 = StarShip((10, -370))
starship_2.shapesize(stretch_wid=0.5, stretch_len=1)
starship_2.color('orange')
starship_2.shape('circle')

starship_3 = StarShip((15, -370))
starship_3.shapesize(stretch_wid=1, stretch_len=0.3)
starship_3.color('white')
starship_3.shape('circle')

starship_4 = StarShip((20, -370))
starship_4.shapesize(stretch_wid=0.5, stretch_len=1)
starship_4.color('orange')
starship_4.shape('circle')

starship_5 = StarShip((30, -370))
starship_5.shapesize(stretch_wid=1.5, stretch_len=0.3)
starship_5.color('white')
starship_5.shape('circle')

# ------------------------------------------------THE SECOND WING-------------------------------------------------------

starship_6 = StarShip((-10, -370))
starship_6.shapesize(stretch_wid=0.5, stretch_len=1)
starship_6.color('orange')
starship_6.shape('circle')

starship_7 = StarShip((-15, -370))
starship_7.shapesize(stretch_wid=1, stretch_len=0.3)
starship_7.color('white')
starship_7.shape('circle')

starship_8 = StarShip((-20, -370))
starship_8.shapesize(stretch_wid=0.5, stretch_len=1)
starship_8.color('orange')
starship_8.shape('circle')

starship_9 = StarShip((-30, -370))
starship_9.shapesize(stretch_wid=1.5, stretch_len=0.3)
starship_9.color('white')
starship_9.shape('circle')

# ----------------------------------------------------THE CABIN---------------------------------------------------------

starship_10 = StarShip((0, -350))
starship_10.shapesize(stretch_wid=1, stretch_len=0.5)
starship_10.color('white')
starship_10.shape('circle')

starship_11 = StarShip((0, -340))
starship_11.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_11.color('blue')
ammo = Ammo()
# ---------------------------------------------STARSHIP FUNCTIONALITY---------------------------------------------------
screen.listen()
screen.onkey(lambda: [starship_1.go_right(), starship_2.go_right(), starship_3.go_right(), starship_4.go_right(),
                      starship_5.go_right(), starship_6.go_right(), starship_7.go_right(), starship_8.go_right(),
                      starship_9.go_right(), starship_10.go_right(), starship_11.go_right()], "Right")
screen.onkey(lambda: [starship_1.go_left(), starship_2.go_left(), starship_3.go_left(), starship_4.go_left(),
                      starship_5.go_left(), starship_6.go_left(), starship_7.go_left(), starship_8.go_left(),
                      starship_9.go_left(), starship_10.go_left(), starship_11.go_left()], "Left")

boss_round_on = True
x_positions = [-600, -550, -400, -350, -200, -150, -50, 0, 50, 150, 200, 350, 400, 550, 600]

gray_blocks = []
red_blocks = []

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=0)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-80)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-60)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-40)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-20)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-40)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-60)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=-80)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    red_block = Turtle(shape="square")
    red_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    red_block.penup()
    red_block.color('red')
    red_block.goto(x=x_positions[block], y=-100)
    red_blocks.append(red_block)

for block in range(0, 15):
    red_block = Turtle(shape="square")
    red_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    red_block.penup()
    red_block.color('red')
    red_block.goto(x=x_positions[block], y=-120)
    red_blocks.append(red_block)

boss_lives = 10

while boss_round_on:

    screen.update()

    ammo.shoot()
    screen.onkey(lambda: [ammo.shoot(), ammo.reset_position(starship_11.xcor(), starship_11.ycor())], "Up")
    time.sleep(ammo.move_speed)

    # --------------------------------------------------------BOSS SHIP 1-----------------------------------------------
    boss.enemy_move_right()

    boss_ammo_one.enemy_shoot()
    boss_ammo_one.left(100)
    if boss_ammo_one.ycor() < -1000:
        boss_ammo_one.reset_position(boss.xcor() - 20, boss.ycor() - 100)

    boss_ammo_two.enemy_shoot()
    boss_ammo_two.left(100)
    if boss_ammo_two.ycor() < -1000:
        boss_ammo_two.reset_position(boss.xcor() + 150, boss.ycor() - 100)

    boss_ammo_three.enemy_shoot()
    boss_ammo_three.left(100)
    if boss_ammo_three.ycor() < -1000:
        boss_ammo_three.reset_position(boss.xcor() + 300, boss.ycor() - 100)

    boss_ammo_four.enemy_shoot()
    boss_ammo_four.left(100)
    if boss_ammo_four.ycor() < -1000:
        boss_ammo_four.reset_position(boss.xcor() - 150, boss.ycor() - 100)

    boss_ammo_five.enemy_shoot()
    boss_ammo_five.left(100)
    if boss_ammo_five.ycor() < -1000:
        boss_ammo_five.reset_position(boss.xcor() - 300, boss.ycor() - 100)

    boss_ammo_six.enemy_shoot()
    boss_ammo_six.left(100)
    if boss_ammo_six.ycor() < -1000:
        boss_ammo_six.reset_position(boss.xcor() + 20, boss.ycor() - 100)

    if boss.xcor() == 500 or boss.xcor() == -500:
        boss.bounce()

    # --------------------------------------------------GRAY BLOCKS DEMOLITION------------------------------------------

    for block in gray_blocks:
        if ammo.distance(block) < 25:
            block.goto(1000, -1000)
            ammo.goto(1000, -1000)

    for block in gray_blocks:
        if boss_ammo_one.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_one.goto(1000, -1000)

    for block in gray_blocks:
        if boss_ammo_two.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_two.goto(1000, -1000)

    for block in gray_blocks:
        if boss_ammo_three.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_three.goto(1000, -1000)

    for block in gray_blocks:
        if boss_ammo_four.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_four.goto(1000, -1000)

    for block in gray_blocks:
        if boss_ammo_five.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_five.goto(1000, -1000)

    for block in gray_blocks:
        if boss_ammo_six.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_six.goto(1000, -1000)
    # ------------------------------------------RED BLOCKS DEMOLITION--------------------------------------------------
    for red_block in red_blocks:
        if ammo.distance(red_block) < 25:
            red_block.goto(1000, -1000)
            ammo.goto(1000, -1000)

    for block in red_blocks:
        if boss_ammo_one.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_one.goto(1000, -1000)

    for block in red_blocks:
        if boss_ammo_two.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_two.goto(1000, -1000)

    for block in red_blocks:
        if boss_ammo_three.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_three.goto(1000, -1000)

    for block in red_blocks:
        if boss_ammo_four.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_four.goto(1000, -1000)

    for block in red_blocks:
        if boss_ammo_five.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_five.goto(1000, -1000)

    for block in red_blocks:
        if boss_ammo_six.distance(block) < 25:
            block.goto(1000, -1000)
            boss_ammo_six.goto(1000, -1000)

    # ---------------------------------------------FIGHT THE BOSS FUNCTIONAL------------------------------------------------

    if ammo.distance(boss) < 50:
        ammo.reset_position(1000, -1000)
        boss_lives -= 1

    if boss_ammo_one.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif boss_ammo_one.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif boss_ammo_one.distance(starship_1) < 10:
        starship_1.goto(1000, -1000)
        starship_2.goto(1000, -1000)
        starship_3.goto(1000, -1000)
        starship_4.goto(1000, -1000)
        starship_5.goto(1000, -1000)
        starship_6.goto(1000, -1000)
        starship_7.goto(1000, -1000)
        starship_8.goto(1000, -1000)
        starship_9.goto(1000, -1000)
        starship_10.goto(1000, -1000)
        starship_11.goto(1000, -1000)
        print('you lost')

    if boss_ammo_two.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif boss_ammo_two.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif boss_ammo_two.distance(starship_1) < 10:
        starship_1.goto(1000, -1000)
        starship_2.goto(1000, -1000)
        starship_3.goto(1000, -1000)
        starship_4.goto(1000, -1000)
        starship_5.goto(1000, -1000)
        starship_6.goto(1000, -1000)
        starship_7.goto(1000, -1000)
        starship_8.goto(1000, -1000)
        starship_9.goto(1000, -1000)
        starship_10.goto(1000, -1000)
        starship_11.goto(1000, -1000)
        print('you lost')

    if boss_ammo_three.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif boss_ammo_three.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif boss_ammo_three.distance(starship_1) < 10:
        starship_1.goto(1000, -1000)
        starship_2.goto(1000, -1000)
        starship_3.goto(1000, -1000)
        starship_4.goto(1000, -1000)
        starship_5.goto(1000, -1000)
        starship_6.goto(1000, -1000)
        starship_7.goto(1000, -1000)
        starship_8.goto(1000, -1000)
        starship_9.goto(1000, -1000)
        starship_10.goto(1000, -1000)
        starship_11.goto(1000, -1000)
        print('you lost')

    if boss_ammo_four.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif boss_ammo_four.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif boss_ammo_four.distance(starship_1) < 10:
        starship_1.goto(1000, -1000)
        starship_2.goto(1000, -1000)
        starship_3.goto(1000, -1000)
        starship_4.goto(1000, -1000)
        starship_5.goto(1000, -1000)
        starship_6.goto(1000, -1000)
        starship_7.goto(1000, -1000)
        starship_8.goto(1000, -1000)
        starship_9.goto(1000, -1000)
        starship_10.goto(1000, -1000)
        starship_11.goto(1000, -1000)
        print('you lost')

    if boss_ammo_five.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif boss_ammo_five.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif boss_ammo_five.distance(starship_1) < 10:
        starship_1.goto(1000, -1000)
        starship_2.goto(1000, -1000)
        starship_3.goto(1000, -1000)
        starship_4.goto(1000, -1000)
        starship_5.goto(1000, -1000)
        starship_6.goto(1000, -1000)
        starship_7.goto(1000, -1000)
        starship_8.goto(1000, -1000)
        starship_9.goto(1000, -1000)
        starship_10.goto(1000, -1000)
        starship_11.goto(1000, -1000)
        print('you lost')

    if boss_ammo_six.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif boss_ammo_six.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif boss_ammo_six.distance(starship_1) < 10:
        starship_1.goto(1000, -1000)
        starship_2.goto(1000, -1000)
        starship_3.goto(1000, -1000)
        starship_4.goto(1000, -1000)
        starship_5.goto(1000, -1000)
        starship_6.goto(1000, -1000)
        starship_7.goto(1000, -1000)
        starship_8.goto(1000, -1000)
        starship_9.goto(1000, -1000)
        starship_10.goto(1000, -1000)
        starship_11.goto(1000, -1000)
        print('you lost')

    if boss_lives == 0:
        boss.goto(1000, -1000)
        print('you won')



screen.exitonclick()
