import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor('lightblue')

p1 = turtle.getturtle()
p1.color('green')
p1.shape('turtle')
p1.penup()
p1.goto(-300, 200,)


p2 = p1.clone()
p2.color('red')
p2.goto(-300, -200)

p1.goto(300, -250)
p1.left(90)
p1.pendown()
p1.color('black')
p1.forward(500)
p1.write('FINISH!', font= 50)
p1.penup()
p1.goto(-300, 200)
p1.color('green')
p1.right(90)

p1.pendown()
p2.pendown()

dice = [1, 2, 3, 4, 5, 6]

for i in range(30):
    if p1.pos() >= (300, 250):
        print("player one wins the game!!")
        break
    elif p2.pos() >= (300, -250):
        print("player two wins the game!!")
        break
    else:
        die_roll = random.choice(dice)
        p1.forward(30 * die_roll)
        time.sleep(1)
        die_roll2 = random.choice(dice)
        p2.forward(30 * die_roll2)
        time.sleep(1)
