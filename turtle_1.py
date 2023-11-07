import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)


# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(50)
carver.pendown()
carver.forward(400)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# eye
carver.penup()
carver.setposition(50,25)
carver.dot(30)

carver.penup()
carver.setposition(-50,25)
carver.dot(30)

# mouth
carver.penup()
carver.setposition(-40, -40)
carver.pensize(15)
carver.pendown()
carver.forward(80)
carver.pensize(1)


turtle.done()