# Ein Quadrat zeichnen - zuerst ohne, dann mit Schleife
import turtle

t = turtle.Turtle()

# Variante 1: jeder Schritt einzeln
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# Turtle versetzen, ohne zu zeichnen
t.penup()
t.goto(150, 0)
t.pendown()

# Variante 2: mit einer for-Schleife
for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
