# Eine Funktion, die jedes regelmaessige Vieleck zeichnen kann
import turtle

t = turtle.Turtle()
t.speed(0)


def vieleck(ecken, laenge, farbe):
    t.color(farbe)
    t.begin_fill()
    for i in range(ecken):
        t.forward(laenge)
        t.left(360 / ecken)
    t.end_fill()


def springe(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


springe(-250, 0)
vieleck(3, 80, "red")

springe(-130, 0)
vieleck(4, 70, "orange")

springe(-20, 0)
vieleck(5, 60, "gold")

springe(100, 0)
vieleck(6, 50, "green")

springe(220, 0)
vieleck(8, 35, "blue")

t.hideturtle()
turtle.done()
