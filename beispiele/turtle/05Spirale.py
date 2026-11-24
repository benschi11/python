# Eine eckige Spirale: die Strecke wird bei jedem Durchlauf laenger
import turtle

t = turtle.Turtle()
t.speed(0)

laenge = 5
for i in range(60):
    t.forward(laenge)
    t.left(91)          # probiere auch 90, 121 oder 144
    laenge = laenge + 5

t.hideturtle()
turtle.done()
