import turtle

t = turtle.Turtle()

# 1. Cuadrado rojo sin rellenar
t.color("red")
t.penup()
t.goto(-150, 0)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.left(90)

# 2. Círculo verde relleno
t.color("green")
t.penup()
t.goto(100, 0)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.hideturtle()
turtle.done()

# Hecho con Gemini
