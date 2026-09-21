import math
import turtle

amp = 150
frekvence = 1
tlumeni = 0.3

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.penup(); t.goto(-350, 0); t.pendown(); t.goto(350, 0)
t.penup(); t.goto(-350, 0); t.pendown()

t.pencolor("red")
t.pensize(10)
for i in range(700):
    cas = i / 100
    y = amplituda * math.sin(2 * math.pi * frekvence * cas) * math.exp(-tlumeni * cas)
    t.goto(-350 + i, y)

turtle.done()
