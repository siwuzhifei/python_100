import turtle
import random


tim = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(90)
        tim.setheading(tim.heading() + size_of_gap)


tim.speed(10)
draw_spirograph(10)


screen.exitonclick()