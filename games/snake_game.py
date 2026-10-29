import turtle
import time
import random
import tkinter as tk

class eTurtle(turtle.Turtle):
    dir = 'up'
    last_dir = 'up'

sc = turtle.Screen()
sc.title("Snakesss")
sc.bgcolor("black")
sc.tracer(0)
sc.screensize(100,100)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
# head.direction("stop")

x_food = 0
y_food = 100

food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.goto(x_food,y_food)

segments = []
direction = "up"
score = 0
high_score = 0
STEPS = 20
DELAY = .1

screen_width = 400
screen_height = 400

x_offset = 0
y_offset = 0

root = tk.Tk()
root.withdraw()
SCREEN_MID_X = root.winfo_screenwidth()/2
SCREEN_MID_Y = root.winfo_screenheight()/2
root.destroy()

rect = turtle.Turtle()
rect.speed(0)
rect.pencolor("white")
rect.width(5)

def draw_limit():
    rect.clear()
    rect.penup()
    rect.goto(SCREEN_MID_X-screen_width/2-x_offset,SCREEN_MID_Y-y_offset)
    # rect.goto(100-x_offset,100-y_offset)
    rect.pendown()
    rect.goto(SCREEN_MID_X+screen_width/2-x_offset,SCREEN_MID_Y-y_offset)
    # rect.goto(-100-x_offset,100-y_offset)

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

def move():
    global y_offset
    global x_offset
    match direction:
        case "up":
            y_offset += STEPS
        case "down":
            y_offset -= STEPS
        case "left":
            x_offset -= STEPS
        case "right":
            x_offset += STEPS

def move_food():
    food.goto(x_food-x_offset, y_food-y_offset)

def move_first_segment():
    match direction:
        case "up":
            segments[0].goto(0,-STEPS)
        case "down":
            segments[0].goto(0,STEPS)
        case "left":
            segments[0].goto(STEPS,0)
        case "right":
            segments[0].goto(-STEPS,0)
    segments[0].last_dir = segments[0].dir
    segments[0].dir = direction

sc.listen()
sc.onkeypress(go_up, "w")
sc.onkeypress(go_left, "a")
sc.onkeypress(go_down, "s")
sc.onkeypress(go_right, "d")

while True:
    sc.update()
    sc.setup(
        screen_width, 
        screen_height, 
        startx=SCREEN_MID_X-(screen_width/2)+x_offset, 
        starty=SCREEN_MID_Y-(screen_height/2)-y_offset
    )
    # print(startx*SCREEN_MULTIPLIER)
    # print(head.xcor())
    
    if len(segments) > 0: 
        move_first_segment()
    for i in range(1, len(segments), 1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        last_dir = segments[i-1].last_dir
        match last_dir:
            case "up":
                segments[i].goto(x,y-STEPS)
            case "down":
                segments[i].goto(x,y+STEPS)
            case "left":
                segments[i].goto(x+STEPS,y)
            case "right":
                segments[i].goto(x-STEPS,y)
        segments[i].last_dir = segments[i].dir
        segments[i].dir = last_dir


    # if snake takes food
    if head.distance(food) < 20:
        x_food = random.randint(-100, 100)
        y_food = random.randint(-100, 100)
        # x_food = random.randint(-screen_width, screen_width)
        # y_food = random.randint(-screen_height, screen_height)

        new_segment = eTurtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('lightgreen')
        new_segment.penup()
        segments.append(new_segment)
        score += 1
        
    move()
    move_food()
    draw_limit()
    time.sleep(DELAY)