import turtle
import random
screen=turtle.Screen()
screen.bgcolor('black')
shape=turtle.Turtle()
shape.color('white')
shape.speed(200)
side=10
colors=['red','blue','yellow','green','orange','violet']
for i in range(50):
    shape.color(random.choice(colors))
    for j in range (50):
        shape.forward(side)
        shape.left(90)
        shape.forward(side)
        shape.left(90)
        side=side+10