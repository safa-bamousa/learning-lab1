from turtle import Turtle, Screen
#mouraba3
sam = Turtle()
sam.shape("turtle") #square, triangle, circle, classic, arrow
sam.color("red")
for _ in range(4):
    sam.forward(100)
    sam.left(90)

#moutalat
sam = Turtle()
sam.shape("turtle")
sam.color("red")
for _ in range(3):
    sam.forward(100)
    sam.left(120)

#da2ira
sam.speed("fastest")
sam = Turtle()
sam.shape("turtle")
sam.color("red")
for _ in range(360):
    sam.forward(1)
    sam.left(1)

#da2ira
sam.circle(100)

sam.penup()
sam.forward(100)
sam.pendown()
sam.pensize(10)
sam.forward(50)


window = Screen()
window.exitonclick()
