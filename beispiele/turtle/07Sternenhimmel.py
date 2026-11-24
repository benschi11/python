# Ein Sternenhimmel mit zufaelligen Positionen, Groessen und Farben
import turtle
import random

turtle.bgcolor("midnightblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

farben = ["white", "yellow", "lightyellow", "lightblue"]


def stern(groesse, farbe):
    t.color(farbe)
    t.begin_fill()
    for i in range(5):
        t.forward(groesse)
        t.right(144)
    t.end_fill()


for i in range(40):
    x = random.randint(-300, 280)
    y = random.randint(-250, 250)
    t.penup()
    t.goto(x, y)
    t.pendown()
    stern(random.randint(5, 30), random.choice(farben))

turtle.done()
