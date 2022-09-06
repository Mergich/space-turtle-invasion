import random
from turtle import Turtle
from turtle import Screen
from starship import StarShip
from ammo import Ammo
import time
from boss import Boss
from scoreboard import GameOver
from stars import StarManager
from random import randint

MOVE_DISTANCE = 70

# -------------------------------------------------PLAY SCREEN----------------------------------------------------------
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1300, height=900)
screen.title("Space Turtle Invasion")
screen.tracer(0)

# -----------------------------------------------STARSHIP CONTROLLER----------------------------------------------------
starship_1 = StarShip((200, -360))
# ------------------------------------------------THE FIRST WING--------------------------------------------------------

starship_2 = StarShip((210, -370))
starship_2.shapesize(stretch_wid=0.5, stretch_len=1)
starship_2.color('orange')
starship_2.shape('circle')

starship_3 = StarShip((215, -370))
starship_3.shapesize(stretch_wid=1, stretch_len=0.3)
starship_3.color('white')
starship_3.shape('circle')

starship_4 = StarShip((220, -370))
starship_4.shapesize(stretch_wid=0.5, stretch_len=1)
starship_4.color('orange')
starship_4.shape('circle')

starship_5 = StarShip((230, -370))
starship_5.shapesize(stretch_wid=1.5, stretch_len=0.3)
starship_5.color('white')
starship_5.shape('circle')

# ------------------------------------------------THE SECOND WING-------------------------------------------------------

starship_6 = StarShip((190, -370))
starship_6.shapesize(stretch_wid=0.5, stretch_len=1)
starship_6.color('orange')
starship_6.shape('circle')

starship_7 = StarShip((185, -370))
starship_7.shapesize(stretch_wid=1, stretch_len=0.3)
starship_7.color('white')
starship_7.shape('circle')

starship_8 = StarShip((180, -370))
starship_8.shapesize(stretch_wid=0.5, stretch_len=1)
starship_8.color('orange')
starship_8.shape('circle')

starship_9 = StarShip((170, -370))
starship_9.shapesize(stretch_wid=1.5, stretch_len=0.3)
starship_9.color('white')
starship_9.shape('circle')

# ----------------------------------------------------THE CABIN---------------------------------------------------------

starship_10 = StarShip((200, -350))
starship_10.shapesize(stretch_wid=1, stretch_len=0.5)
starship_10.color('white')
starship_10.shape('circle')

starship_11 = StarShip((200, -340))
starship_11.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_11.color('blue')

# ---------------------------------------------STARSHIP FUNCTIONALITY---------------------------------------------------
screen.listen()
screen.onkey(lambda: [starship_1.go_right(), starship_2.go_right(), starship_3.go_right(), starship_4.go_right(),
                      starship_5.go_right(), starship_6.go_right(), starship_7.go_right(), starship_8.go_right(),
                      starship_9.go_right(), starship_10.go_right(), starship_11.go_right()], "Right")
screen.onkey(lambda: [starship_1.go_left(), starship_2.go_left(), starship_3.go_left(), starship_4.go_left(),
                      starship_5.go_left(), starship_6.go_left(), starship_7.go_left(), starship_8.go_left(),
                      starship_9.go_left(), starship_10.go_left(), starship_11.go_left()], "Left")
# ----------------------------------------------------STARSHIP AMMO-----------------------------------------------------
ammo = Ammo()
# ----------------------------------------------ENEMY SHIP # 1----------------------------------------------------------
starship_16 = StarShip((50, 150))
starship_16.shapesize(stretch_wid=1, stretch_len=1)
starship_16.color('gray')
starship_16.shape('circle')

starship_17 = StarShip((50, 140))
starship_17.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_17.color('red')

starship_18 = StarShip((70, 150))
starship_18.shapesize(stretch_wid=2, stretch_len=0.2)
starship_18.color('darkred')
starship_18.shape('circle')

starship_19 = StarShip((30, 150))
starship_19.shapesize(stretch_wid=2, stretch_len=0.2)
starship_19.color('darkred')
starship_19.shape('circle')

starship_20 = StarShip((65, 150))
starship_20.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_20.color('gray')
starship_20.shape('square')

starship_21 = StarShip((35, 150))
starship_21.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_21.color('gray')
starship_21.shape('square')

enemy_starship_one_ammo = Ammo()
enemy_starship_one_ammo.color('red')
enemy_starship_one_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)

# ----------------------------------------------ENEMY SHIP # 2----------------------------------------------------------
starship_22 = StarShip((-100, 200))
starship_22.shapesize(stretch_wid=1, stretch_len=1)
starship_22.color('gray')
starship_22.shape('circle')

starship_23 = StarShip((-100, 190))
starship_23.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_23.color('red')

starship_24 = StarShip((-80, 200))
starship_24.shapesize(stretch_wid=2, stretch_len=0.2)
starship_24.color('darkred')
starship_24.shape('circle')

starship_25 = StarShip((-120, 200))
starship_25.shapesize(stretch_wid=2, stretch_len=0.2)
starship_25.color('darkred')
starship_25.shape('circle')

starship_26 = StarShip((-85, 200))
starship_26.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_26.color('gray')
starship_26.shape('square')

starship_27 = StarShip((-115, 200))
starship_27.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_27.color('gray')
starship_27.shape('square')

enemy_starship_two_ammo = Ammo()
enemy_starship_two_ammo.color('red')
enemy_starship_two_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)
# ----------------------------------------------ENEMY SHIP # 3----------------------------------------------------------
starship_28 = StarShip((100, 250))
starship_28.shapesize(stretch_wid=1, stretch_len=1)
starship_28.color('gray')
starship_28.shape('circle')

starship_29 = StarShip((100, 240))
starship_29.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_29.color('red')

starship_30 = StarShip((120, 250))
starship_30.shapesize(stretch_wid=2, stretch_len=0.2)
starship_30.color('darkred')
starship_30.shape('circle')

starship_31 = StarShip((80, 250))
starship_31.shapesize(stretch_wid=2, stretch_len=0.2)
starship_31.color('darkred')
starship_31.shape('circle')

starship_32 = StarShip((115, 250))
starship_32.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_32.color('gray')
starship_32.shape('square')

starship_33 = StarShip((85, 250))
starship_33.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_33.color('gray')
starship_33.shape('square')

enemy_starship_three_ammo = Ammo()
enemy_starship_three_ammo.color('red')
enemy_starship_three_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)
# ----------------------------------------------ENEMY SHIP # 4----------------------------------------------------------
starship_34 = StarShip((300, 300))
starship_34.shapesize(stretch_wid=1, stretch_len=1)
starship_34.color('gray')
starship_34.shape('circle')

starship_35 = StarShip((300, 290))
starship_35.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_35.color('red')

starship_36 = StarShip((320, 300))
starship_36.shapesize(stretch_wid=2, stretch_len=0.2)
starship_36.color('darkred')
starship_36.shape('circle')

starship_37 = StarShip((280, 300))
starship_37.shapesize(stretch_wid=2, stretch_len=0.2)
starship_37.color('darkred')
starship_37.shape('circle')

starship_38 = StarShip((315, 300))
starship_38.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_38.color('gray')
starship_38.shape('square')

starship_39 = StarShip((285, 300))
starship_39.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_39.color('gray')
starship_39.shape('square')

enemy_starship_four_ammo = Ammo()
enemy_starship_four_ammo.color('red')
enemy_starship_four_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)
# ----------------------------------------------ENEMY SHIP # 5----------------------------------------------------------
starship_40 = StarShip((-300, 350))
starship_40.shapesize(stretch_wid=1, stretch_len=1)
starship_40.color('gray')
starship_40.shape('circle')

starship_41 = StarShip((-300, 340))
starship_41.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_41.color('red')

starship_42 = StarShip((-320, 350))
starship_42.shapesize(stretch_wid=2, stretch_len=0.2)
starship_42.color('darkred')
starship_42.shape('circle')

starship_43 = StarShip((-280, 350))
starship_43.shapesize(stretch_wid=2, stretch_len=0.2)
starship_43.color('darkred')
starship_43.shape('circle')

starship_44 = StarShip((-315, 350))
starship_44.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_44.color('gray')
starship_44.shape('square')

starship_45 = StarShip((-285, 350))
starship_45.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_45.color('gray')
starship_45.shape('square')

enemy_starship_five_ammo = Ammo()
enemy_starship_five_ammo.color('red')
enemy_starship_five_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)

# ----------------------------------------------ENEMY SHIP # 6----------------------------------------------------------
starship_46 = StarShip((200, 150))
starship_46.shapesize(stretch_wid=1, stretch_len=1)
starship_46.color('gray')
starship_46.shape('circle')

starship_47 = StarShip((200, 140))
starship_47.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_47.color('red')

starship_48 = StarShip((220, 150))
starship_48.shapesize(stretch_wid=2, stretch_len=0.2)
starship_48.color('darkred')
starship_48.shape('circle')

starship_49 = StarShip((180, 150))
starship_49.shapesize(stretch_wid=2, stretch_len=0.2)
starship_49.color('darkred')
starship_49.shape('circle')

starship_50 = StarShip((215, 150))
starship_50.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_50.color('gray')
starship_50.shape('square')

starship_51 = StarShip((185, 150))
starship_51.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_51.color('gray')
starship_51.shape('square')

enemy_starship_six_ammo = Ammo()
enemy_starship_six_ammo.color('red')
enemy_starship_six_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)

# ----------------------------------------------ENEMY SHIP # 7----------------------------------------------------------
starship_52 = StarShip((-200, 200))
starship_52.shapesize(stretch_wid=1, stretch_len=1)
starship_52.color('gray')
starship_52.shape('circle')

starship_53 = StarShip((-200, 190))
starship_53.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_53.color('red')

starship_54 = StarShip((-180, 200))
starship_54.shapesize(stretch_wid=2, stretch_len=0.2)
starship_54.color('darkred')
starship_54.shape('circle')

starship_55 = StarShip((-220, 200))
starship_55.shapesize(stretch_wid=2, stretch_len=0.2)
starship_55.color('darkred')
starship_55.shape('circle')

starship_56 = StarShip((-185, 200))
starship_56.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_56.color('gray')
starship_56.shape('square')

starship_57 = StarShip((-215, 200))
starship_57.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_57.color('gray')
starship_57.shape('square')

enemy_starship_seven_ammo = Ammo()
enemy_starship_seven_ammo.color('red')
enemy_starship_seven_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)
# ----------------------------------------------ENEMY SHIP # 8----------------------------------------------------------
starship_58 = StarShip((400, 250))
starship_58.shapesize(stretch_wid=1, stretch_len=1)
starship_58.color('gray')
starship_58.shape('circle')

starship_59 = StarShip((400, 240))
starship_59.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_59.color('red')

starship_60 = StarShip((420, 250))
starship_60.shapesize(stretch_wid=2, stretch_len=0.2)
starship_60.color('darkred')
starship_60.shape('circle')

starship_61 = StarShip((380, 250))
starship_61.shapesize(stretch_wid=2, stretch_len=0.2)
starship_61.color('darkred')
starship_61.shape('circle')

starship_62 = StarShip((415, 250))
starship_62.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_62.color('gray')
starship_62.shape('square')

starship_63 = StarShip((385, 250))
starship_63.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_63.color('gray')
starship_63.shape('square')

enemy_starship_eight_ammo = Ammo()
enemy_starship_eight_ammo.color('red')
enemy_starship_eight_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)
# ----------------------------------------------ENEMY SHIP # 9----------------------------------------------------------
starship_64 = StarShip((-400, 300))
starship_64.shapesize(stretch_wid=1, stretch_len=1)
starship_64.color('gray')
starship_64.shape('circle')

starship_65 = StarShip((-400, 290))
starship_65.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_65.color('red')

starship_66 = StarShip((-380, 300))
starship_66.shapesize(stretch_wid=2, stretch_len=0.2)
starship_66.color('darkred')
starship_66.shape('circle')

starship_67 = StarShip((-420, 300))
starship_67.shapesize(stretch_wid=2, stretch_len=0.2)
starship_67.color('darkred')
starship_67.shape('circle')

starship_68 = StarShip((-385, 300))
starship_68.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_68.color('gray')
starship_68.shape('square')

starship_69 = StarShip((-415, 300))
starship_69.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_69.color('gray')
starship_69.shape('square')

enemy_starship_nine_ammo = Ammo()
enemy_starship_nine_ammo.color('red')
enemy_starship_nine_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)
# ----------------------------------------------ENEMY SHIP # 10---------------------------------------------------------
starship_70 = StarShip((-50, 350))
starship_70.shapesize(stretch_wid=1, stretch_len=1)
starship_70.color('gray')
starship_70.shape('circle')

starship_71 = StarShip((-50, 340))
starship_71.shapesize(stretch_wid=0.3, stretch_len=0.3)
starship_71.color('red')

starship_72 = StarShip((-70, 350))
starship_72.shapesize(stretch_wid=2, stretch_len=0.2)
starship_72.color('darkred')
starship_72.shape('circle')

starship_73 = StarShip((-30, 350))
starship_73.shapesize(stretch_wid=2, stretch_len=0.2)
starship_73.color('darkred')
starship_73.shape('circle')

starship_74 = StarShip((-65, 350))
starship_74.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_74.color('gray')
starship_74.shape('square')

starship_75 = StarShip((-35, 350))
starship_75.shapesize(stretch_wid=0.2, stretch_len=0.3)
starship_75.color('gray')
starship_75.shape('square')

enemy_starship_ten_ammo = Ammo()
enemy_starship_ten_ammo.color('red')
enemy_starship_ten_ammo.shapesize(stretch_wid=1.2, stretch_len=0.1)

# -------------------------------------------------BOUNDARY CONTROL-----------------------------------------------------
x_positions = [-600, -550, -400, -350, -200, -150, -50, 0, 50, 150, 200, 350, 400, 550, 600]

gray_blocks = []
red_blocks = []

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=100)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=80)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=60)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=40)
    gray_blocks.append(gray_block)

for block in range(0, 15):
    gray_block = Turtle(shape="square")
    gray_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    gray_block.penup()
    gray_block.color('gray')
    gray_block.goto(x=x_positions[block], y=20)
    gray_blocks.append(gray_block)

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
    red_block = Turtle(shape="square")
    red_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    red_block.penup()
    red_block.color('red')
    red_block.goto(x=x_positions[block], y=-60)
    red_blocks.append(red_block)

for block in range(0, 15):
    red_block = Turtle(shape="square")
    red_block.shapesize(stretch_wid=0.8, stretch_len=2.1)
    red_block.penup()
    red_block.color('red')
    red_block.goto(x=x_positions[block], y=-80)
    red_blocks.append(red_block)
# ---------------------------------------------------STAR CONTROL-------------------------------------------------------
for block in range(100):
    new_star = Turtle("square")
    new_star.shapesize(stretch_wid=0.01, stretch_len=0.01)
    new_star.penup()
    new_star.color('white')
    random_y = random.randint(-450, 450)
    random_x = random.randint(-650, 650)
    new_star.goto(random_x, random_y)
# ----------------------------------------------------------------------------------------------------------------------
game_is_on = True
lives = 11
game_over = GameOver()
while game_is_on:

    screen.update()

    ammo.shoot()
    screen.onkey(lambda: [ammo.shoot(), ammo.reset_position(starship_11.xcor(), starship_11.ycor())], "Up")
    time.sleep(ammo.move_speed)

    # ---------------------------------------------------ENEMY SHIP 1---------------------------------------------------
    (starship_16.enemy_move_right(), starship_17.enemy_move_right(), starship_18.enemy_move_right(),
     starship_19.enemy_move_right(), starship_20.enemy_move_right(), starship_21.enemy_move_right())
    enemy_starship_one_ammo.enemy_shoot()
    if enemy_starship_one_ammo.ycor() < -800:
        enemy_starship_one_ammo.reset_position(starship_17.xcor(), starship_17.ycor())

    if starship_16.xcor() == 600 or starship_16.xcor() == -600:
        (starship_16.bounce(), starship_17.bounce(), starship_18.bounce(),
         starship_19.bounce(), starship_20.bounce(), starship_21.bounce())

    # ---------------------------------------------------ENEMY SHIP 2---------------------------------------------------
    (starship_22.enemy_move_left(), starship_23.enemy_move_left(), starship_24.enemy_move_left(),
     starship_25.enemy_move_left(), starship_26.enemy_move_left(), starship_27.enemy_move_left())
    enemy_starship_two_ammo.enemy_shoot()
    if enemy_starship_two_ammo.ycor() < -800:
        enemy_starship_two_ammo.reset_position(starship_23.xcor(), starship_23.ycor())

    if starship_22.xcor() == 600 or starship_22.xcor() == -600:
        (starship_22.bounce(), starship_23.bounce(), starship_24.bounce(),
         starship_25.bounce(), starship_26.bounce(), starship_27.bounce())
    # ---------------------------------------------------ENEMY SHIP 3---------------------------------------------------
    (starship_28.enemy_move_right(), starship_29.enemy_move_right(), starship_30.enemy_move_right(),
     starship_31.enemy_move_right(), starship_32.enemy_move_right(), starship_33.enemy_move_right())
    enemy_starship_three_ammo.enemy_shoot()
    if enemy_starship_three_ammo.ycor() < -800:
        enemy_starship_three_ammo.reset_position(starship_29.xcor(), starship_29.ycor())

    if starship_28.xcor() == 600 or starship_28.xcor() == -600:
        (starship_28.bounce(), starship_29.bounce(), starship_30.bounce(),
         starship_31.bounce(), starship_32.bounce(), starship_33.bounce())
    # ---------------------------------------------------ENEMY SHIP 4---------------------------------------------------
    (starship_34.enemy_move_left(), starship_35.enemy_move_left(), starship_36.enemy_move_left(),
     starship_37.enemy_move_left(), starship_38.enemy_move_left(), starship_39.enemy_move_left())
    enemy_starship_four_ammo.enemy_shoot()
    if enemy_starship_four_ammo.ycor() < -800:
        enemy_starship_four_ammo.reset_position(starship_35.xcor(), starship_35.ycor())

    if starship_34.xcor() == 600 or starship_34.xcor() == -600:
        (starship_34.bounce(), starship_35.bounce(), starship_36.bounce(),
         starship_37.bounce(), starship_38.bounce(), starship_39.bounce())
    # ---------------------------------------------------ENEMY SHIP 5---------------------------------------------------
    (starship_40.enemy_move_right(), starship_41.enemy_move_right(), starship_42.enemy_move_right(),
     starship_43.enemy_move_right(), starship_44.enemy_move_right(), starship_45.enemy_move_right())
    enemy_starship_five_ammo.enemy_shoot()
    if enemy_starship_five_ammo.ycor() < -800:
        enemy_starship_five_ammo.reset_position(starship_41.xcor(), starship_41.ycor())

    if starship_40.xcor() == 600 or starship_40.xcor() == -600:
        (starship_40.bounce(), starship_41.bounce(), starship_42.bounce(),
         starship_43.bounce(), starship_44.bounce(), starship_45.bounce())

    # ---------------------------------------------------ENEMY SHIP 6---------------------------------------------------
    (starship_46.enemy_move_left(), starship_47.enemy_move_left(), starship_48.enemy_move_left(),
     starship_49.enemy_move_left(), starship_50.enemy_move_left(), starship_51.enemy_move_left())
    enemy_starship_six_ammo.enemy_shoot()
    if enemy_starship_six_ammo.ycor() < -800:
        enemy_starship_six_ammo.reset_position(starship_47.xcor(), starship_47.ycor())

    if starship_46.xcor() == 600 or starship_46.xcor() == -600:
        (starship_46.bounce(), starship_47.bounce(), starship_48.bounce(),
         starship_49.bounce(), starship_50.bounce(), starship_51.bounce())

    # ---------------------------------------------------ENEMY SHIP 7---------------------------------------------------
    (starship_52.enemy_move_right(), starship_53.enemy_move_right(), starship_54.enemy_move_right(),
     starship_55.enemy_move_right(), starship_56.enemy_move_right(), starship_57.enemy_move_right())
    enemy_starship_seven_ammo.enemy_shoot()
    if enemy_starship_seven_ammo.ycor() < -800:
        enemy_starship_seven_ammo.reset_position(starship_53.xcor(), starship_53.ycor())

    if starship_52.xcor() == 600 or starship_52.xcor() == -600:
        (starship_52.bounce(), starship_53.bounce(), starship_54.bounce(),
         starship_55.bounce(), starship_56.bounce(), starship_57.bounce())
    # ---------------------------------------------------ENEMY SHIP 8---------------------------------------------------
    (starship_58.enemy_move_left(), starship_59.enemy_move_left(), starship_60.enemy_move_left(),
     starship_61.enemy_move_left(), starship_62.enemy_move_left(), starship_63.enemy_move_left())
    enemy_starship_eight_ammo.enemy_shoot()
    if enemy_starship_eight_ammo.ycor() < -800:
        enemy_starship_eight_ammo.reset_position(starship_59.xcor(), starship_59.ycor())

    if starship_58.xcor() == 600 or starship_58.xcor() == -600:
        (starship_58.bounce(), starship_59.bounce(), starship_60.bounce(),
         starship_61.bounce(), starship_62.bounce(), starship_63.bounce())
    # ---------------------------------------------------ENEMY SHIP 9---------------------------------------------------
    (starship_64.enemy_move_right(), starship_65.enemy_move_right(), starship_66.enemy_move_right(),
     starship_67.enemy_move_right(), starship_68.enemy_move_right(), starship_69.enemy_move_right())
    enemy_starship_nine_ammo.enemy_shoot()
    if enemy_starship_nine_ammo.ycor() < -800:
        enemy_starship_nine_ammo.reset_position(starship_65.xcor(), starship_65.ycor())

    if starship_64.xcor() == 600 or starship_64.xcor() == -600:
        (starship_64.bounce(), starship_65.bounce(), starship_66.bounce(),
         starship_67.bounce(), starship_68.bounce(), starship_69.bounce())
    # ---------------------------------------------------ENEMY SHIP 10--------------------------------------------------
    (starship_70.enemy_move_left(), starship_71.enemy_move_left(), starship_72.enemy_move_left(),
     starship_73.enemy_move_left(), starship_74.enemy_move_left(), starship_75.enemy_move_left())
    enemy_starship_ten_ammo.enemy_shoot()
    if enemy_starship_ten_ammo.ycor() < -800:
        enemy_starship_ten_ammo.reset_position(starship_71.xcor(), starship_71.ycor())

    if starship_70.xcor() == 600 or starship_70.xcor() == -600:
        (starship_70.bounce(), starship_71.bounce(), starship_72.bounce(),
         starship_73.bounce(), starship_74.bounce(), starship_75.bounce())

    # --------------------------------------------------GRAY BLOCKS DEMOLITION------------------------------------------

    for block in gray_blocks:
        if ammo.distance(block) < 25:
            block.goto(1000, -1000)
            ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_one_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_one_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_two_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_two_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_three_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_three_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_four_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_four_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_five_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_five_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_six_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_six_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_seven_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_seven_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_eight_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_eight_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_nine_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_nine_ammo.goto(1000, -1000)

    for block in gray_blocks:
        if enemy_starship_ten_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_ten_ammo.goto(1000, -1000)
    # ------------------------------------------RED BLOCKS DEMOLITION--------------------------------------------------
    for red_block in red_blocks:
        if ammo.distance(red_block) < 25:
            red_block.goto(1000, -1000)
            ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_one_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_one_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_two_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_two_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_three_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_three_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_four_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_four_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_five_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_five_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_six_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_six_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_seven_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_seven_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_eight_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_eight_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_nine_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_nine_ammo.goto(1000, -1000)

    for block in red_blocks:
        if enemy_starship_ten_ammo.distance(block) < 25:
            block.goto(1000, -1000)
            enemy_starship_ten_ammo.goto(1000, -1000)

    # -----------------------------ENEMY SHIP 1 DEMOLITION AND ENEMY SHIP ATTACK----------------------------------------
    # attack the wing at first
    if ammo.distance(starship_18) < 7:
        starship_18.goto(1000, -1000)
    elif ammo.distance(starship_19) < 7:
        starship_19.goto(1000, -1000)
    elif ammo.distance(starship_16) < 10:
        starship_16.goto(1000, -1000)
        starship_17.goto(1000, -1000)
        starship_18.goto(1000, -1000)
        starship_19.goto(1000, -1000)
        starship_20.goto(1000, -1000)
        starship_21.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_one_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_one_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_one_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()

    # --------------------------------------------ENEMY SHIP 2 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_24) < 7:
        starship_24.goto(1000, -1000)
    elif ammo.distance(starship_25) < 7:
        starship_25.goto(1000, -1000)
    elif ammo.distance(starship_22) < 10:
        starship_22.goto(1000, -1000)
        starship_23.goto(1000, -1000)
        starship_24.goto(1000, -1000)
        starship_25.goto(1000, -1000)
        starship_26.goto(1000, -1000)
        starship_27.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_two_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_two_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_two_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 3 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_30) < 7:
        starship_30.goto(1000, -1000)
    elif ammo.distance(starship_31) < 7:
        starship_31.goto(1000, -1000)
    elif ammo.distance(starship_28) < 10:
        starship_28.goto(1000, -1000)
        starship_29.goto(1000, -1000)
        starship_30.goto(1000, -1000)
        starship_31.goto(1000, -1000)
        starship_32.goto(1000, -1000)
        starship_33.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_three_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_three_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_three_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 4 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_36) < 7:
        starship_36.goto(1000, -1000)
    elif ammo.distance(starship_37) < 7:
        starship_37.goto(1000, -1000)
    elif ammo.distance(starship_34) < 10:
        starship_34.goto(1000, -1000)
        starship_35.goto(1000, -1000)
        starship_36.goto(1000, -1000)
        starship_37.goto(1000, -1000)
        starship_38.goto(1000, -1000)
        starship_39.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_four_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_four_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_four_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 5 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_42) < 7:
        starship_42.goto(1000, -1000)
    elif ammo.distance(starship_43) < 7:
        starship_43.goto(1000, -1000)
    elif ammo.distance(starship_40) < 10:
        starship_40.goto(1000, -1000)
        starship_41.goto(1000, -1000)
        starship_42.goto(1000, -1000)
        starship_43.goto(1000, -1000)
        starship_44.goto(1000, -1000)
        starship_45.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_five_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_five_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_five_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 6 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_48) < 7:
        starship_48.goto(1000, -1000)
    elif ammo.distance(starship_49) < 7:
        starship_49.goto(1000, -1000)
    elif ammo.distance(starship_46) < 10:
        starship_46.goto(1000, -1000)
        starship_47.goto(1000, -1000)
        starship_48.goto(1000, -1000)
        starship_49.goto(1000, -1000)
        starship_50.goto(1000, -1000)
        starship_51.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_six_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_six_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_six_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 7 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_54) < 7:
        starship_54.goto(1000, -1000)
    elif ammo.distance(starship_55) < 7:
        starship_55.goto(1000, -1000)
    elif ammo.distance(starship_52) < 10:
        starship_52.goto(1000, -1000)
        starship_53.goto(1000, -1000)
        starship_54.goto(1000, -1000)
        starship_55.goto(1000, -1000)
        starship_56.goto(1000, -1000)
        starship_57.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_seven_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_seven_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_seven_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 8 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_60) < 7:
        starship_60.goto(1000, -1000)
    elif ammo.distance(starship_61) < 7:
        starship_61.goto(1000, -1000)
    elif ammo.distance(starship_58) < 10:
        starship_58.goto(1000, -1000)
        starship_59.goto(1000, -1000)
        starship_60.goto(1000, -1000)
        starship_61.goto(1000, -1000)
        starship_62.goto(1000, -1000)
        starship_63.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_eight_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_eight_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_eight_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 9 DEMOLITION-----------------------------------------------

    if ammo.distance(starship_66) < 7:
        starship_66.goto(1000, -1000)
    elif ammo.distance(starship_67) < 7:
        starship_67.goto(1000, -1000)
    elif ammo.distance(starship_64) < 10:
        starship_64.goto(1000, -1000)
        starship_65.goto(1000, -1000)
        starship_66.goto(1000, -1000)
        starship_67.goto(1000, -1000)
        starship_68.goto(1000, -1000)
        starship_69.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_nine_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_nine_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_nine_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    # --------------------------------------------ENEMY SHIP 10 DEMOLITION----------------------------------------------

    if ammo.distance(starship_72) < 7:
        starship_72.goto(1000, -1000)
    elif ammo.distance(starship_73) < 7:
        starship_73.goto(1000, -1000)
    elif ammo.distance(starship_70) < 10:
        starship_70.goto(1000, -1000)
        starship_71.goto(1000, -1000)
        starship_72.goto(1000, -1000)
        starship_73.goto(1000, -1000)
        starship_74.goto(1000, -1000)
        starship_75.goto(1000, -1000)
        ammo.reset_position(1000, -1000)
        lives -= 1

    if enemy_starship_ten_ammo.distance(starship_5) < 7:
        starship_5.goto(1000, -1000)
        starship_4.goto(1000, -1000)
    elif enemy_starship_ten_ammo.distance(starship_9) < 7:
        starship_9.goto(1000, -1000)
        starship_8.goto(1000, -1000)
    elif enemy_starship_ten_ammo.distance(starship_1) < 10:
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
        game_over.you_lost()
    print(lives)
    if lives == 1:

        enemy_starship_one_ammo.goto(1000, -1000)
        enemy_starship_two_ammo.goto(1000, -1000)
        enemy_starship_three_ammo.goto(1000, -1000)
        enemy_starship_four_ammo.goto(1000, -1000)
        enemy_starship_five_ammo.goto(1000, -1000)
        enemy_starship_six_ammo.goto(1000, -1000)
        enemy_starship_seven_ammo.goto(1000, -1000)
        enemy_starship_eight_ammo.goto(1000, -1000)
        enemy_starship_nine_ammo.goto(1000, -1000)
        enemy_starship_ten_ammo.goto(1000, -1000)

        # --------------------------------------------------BOSS ROUND----------------------------------------------------------
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

        # ---------------------------------------------STARSHIP FUNCTIONALITY---------------------------------------------------
        screen.listen()
        screen.onkey(
            lambda: [starship_1.go_right(), starship_2.go_right(), starship_3.go_right(), starship_4.go_right(),
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
                game_over.you_lost()

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
                game_over.you_lost()

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
                game_over.you_lost()

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
                game_over.you_lost()

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
                game_over.you_lost()

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
                game_over.you_lost()

            if boss_lives == 0:
                boss.goto(1000, -1000)
                game_over.you_won()

        screen.exitonclick()
