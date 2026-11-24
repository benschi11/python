# Kreise, Halbkreise und Punkte
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)


def springe(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# Ein ganzer Kreis mit Radius 50
springe(-200, 0)
t.circle(50)

# Ein Halbkreis (180 Grad)
springe(-50, 0)
t.circle(50, 180)

# Ein Kreis aus 6 Ecken - circle kann auch Vielecke!
t.setheading(0)
springe(80, 0)
t.circle(50, steps=6)

# Ein gefuellter Punkt mit Durchmesser 30
springe(250, 50)
t.dot(30, "red")

# Beschriftung
springe(0, -120)
t.write("circle und dot", align="center", font=("Arial", 16, "normal"))

t.hideturtle()
turtle.done()
