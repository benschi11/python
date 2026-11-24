# Ein Haus aus Quadrat, Dreieck und Rechtecken
import turtle

t = turtle.Turtle()
t.speed(0)


def springe(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def vieleck(ecken, laenge, farbe):
    t.color("black", farbe)
    t.begin_fill()
    for i in range(ecken):
        t.forward(laenge)
        t.left(360 / ecken)
    t.end_fill()


def rechteck(breite, hoehe, farbe):
    t.color("black", farbe)
    t.begin_fill()
    for i in range(2):
        t.forward(breite)
        t.left(90)
        t.forward(hoehe)
        t.left(90)
    t.end_fill()


# Wand
springe(-100, -100)
vieleck(4, 200, "lightyellow")

# Dach
springe(-100, 100)
vieleck(3, 200, "firebrick")

# Tuer
springe(-25, -100)
rechteck(50, 90, "saddlebrown")

# Fenster
springe(-80, 20)
rechteck(50, 50, "lightblue")
springe(30, 20)
rechteck(50, 50, "lightblue")

t.hideturtle()
turtle.done()
