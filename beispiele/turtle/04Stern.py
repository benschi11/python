# Ein fuenfzackiger Stern: 5 * 144 Grad = 720 Grad = zwei volle Umdrehungen
import turtle

t = turtle.Turtle()
t.color("darkorange", "gold")
t.pensize(3)

t.penup()
t.goto(-100, 30)
t.pendown()

t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()
