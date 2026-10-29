import turtle
import time
import random

sc = turtle.Screen()
sc.title("Snakesss")
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
# head.direction("stop")

food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)

while True:
    sc.update()