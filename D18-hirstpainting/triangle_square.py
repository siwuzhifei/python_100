import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(2)

for i in range(3, 10):
    for _ in range(i):
        angle = int(360/i)
        tim.forward(100)
        tim.left(angle)