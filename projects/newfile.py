import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255) #allow RGB from 0 t 255
ted = Turtle()

for _ in range(3):
    #random colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ted.color(r, g, b)

    #random shapes
    shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    ted.shape(random.choice(shapes))

    #random size:
    size = random.randint(1,50)
    ted.pensize(size)

    #moves
    ted.forward(100)
    ted.left(90)

#for windows screen
windows = Screen()
windows.exitonclick()