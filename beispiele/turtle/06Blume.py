# Eine Blume aus 36 gedrehten Sechsecken
import turtle

t = turtle.Turtle()
t.speed(0)

farben = ["red", "orange", "gold", "green", "blue", "purple"]


def vieleck(ecken, laenge):
    for i in range(ecken):
        t.forward(laenge)
        t.left(360 / ecken)


for i in range(36):
    t.color(farben[i % len(farben)])
    vieleck(6, 80)
    t.left(10)

t.hideturtle()
turtle.done()
