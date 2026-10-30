import turtle
import time
import random
import tkinter as tk

class eTurtle(turtle.Turtle):
    dir = 'up'
    last_dir = 'up'

def snake_game():
    global direction, score, high_score, screen_width, screen_height, x_offset, y_offset, x_food, y_food, ongoing, game_end
    segments = []
    direction = "up"
    score = 0
    high_score = 0
    ongoing = True
    game_end = False
    STEPS = 20
    INITIAL_DELAY = 1
    DELAY = .1

    screen_width = 250
    screen_height = 250

    x_offset = 0
    y_offset = 0

    x_food = 0
    y_food = 100

    turtle.TurtleScreen._RUNNING = True
    sc = turtle.Screen()
    sc.reset()
    sc.title("Snakesss")
    sc.bgcolor("black")
    sc.tracer(0)
    sc.screensize(100,100)
    sc.cv._rootwindow.resizable(False, False)

    head = turtle.Turtle()
    head.shape("square")
    head.color("green")
    head.penup()
    head.goto(0,0)
    # head.direction("stop")

    food = turtle.Turtle()
    food.color("red")
    food.shape("circle")
    food.penup()
    food.goto(x_food,y_food)

    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.color("green")
    message.goto(0, 290)

    root = tk.Tk()
    root.withdraw()
    SCREEN_MID_X = root.winfo_screenwidth()/2
    SCREEN_MID_Y = root.winfo_screenheight()/2
    root.destroy()

    rect = turtle.Turtle()
    rect.speed(0)
    rect.pencolor("white")
    rect.width(STEPS)
    rect.hideturtle()

    left = -SCREEN_MID_X+screen_width - (-SCREEN_MID_X+screen_width) % STEPS
    right = SCREEN_MID_X-screen_width - (SCREEN_MID_X-screen_width) % STEPS
    top = -SCREEN_MID_Y+screen_height - (-SCREEN_MID_Y+screen_height) % STEPS
    bottom = SCREEN_MID_Y-screen_height - (SCREEN_MID_Y-screen_height) % STEPS

    def trigger_ongoing():
        global ongoing
        ongoing = not ongoing

    def update_score():
        message.clear()
        message.goto(0, screen_height/2-100)
        message.write(
            f"Score: {score}",
            align="center",
            font=("Arial", 16, "bold")
        )

    def draw_limit():
        rect.clear()
        rect.penup()
        rect.goto(left-x_offset,top-y_offset)
        rect.pendown()
        rect.goto(right-x_offset,top-y_offset)
        rect.goto(right-x_offset,bottom-y_offset)
        rect.goto(left-x_offset,bottom-y_offset)
        rect.goto(left-x_offset,top-y_offset)

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

    def check_collision():
        # check for head touching white border or not
        if (left-x_offset>=0 or right-x_offset <= 0 or top-y_offset >= 0 or bottom-y_offset <= 0):
            game_over()

    def welcome():
        global direction
        sc.setup(
            screen_width, 
            screen_height, 
            startx=SCREEN_MID_X-(screen_width/2)+x_offset, 
            starty=SCREEN_MID_Y-(screen_height/2)-y_offset
        )
        draw_limit()
        move_food()
        message.clear()
        message.goto(0, screen_height/2-100)
        message.write(
            "Let's play!",
            align="center",
            font=("Arial", 16, "bold")
        )
        direction = "up"
        sc.update()
        time.sleep(INITIAL_DELAY)

    def game_over():
        global direction, ongoing,high_score
        direction = "stop"
        ongoing = False

        high_score = max(high_score, score)

        message.clear()
        message.goto(-screen_width/2+10, screen_height/2-80)
        message.write(
            f"Game over! Score: {score}\nHigh score: {high_score}\nRestart game? (y/n)",
            align="left",
            font=("Arial", 16, "bold")
        )
        sc.update()
        time.sleep(1)

        sc.onkeypress(trigger_ongoing, "y")
        sc.onkeypress(exit_game, "n")
        sc.listen()

        while not ongoing:
            sc.update()
            if(game_end):
                return

        restart_round()

    def restart_round():
        global score, x_offset,y_offset,x_food,y_food

        sc.onkeypress(None, "y")
        sc.onkeypress(None, "n")

        x_offset = 0
        y_offset = 0
        x_food = 0
        y_food = 100

        for segment in segments:
            segment.hideturtle()

        segments.clear()

        score = 0

        message.clear()
        update_score()

        sc.update()
        welcome()

    def exit_game():
        global game_end
        game_end = True
        print("Snake: bye bye please do come back and visit me hissssssssss")
        print("High score: " + str(high_score))
        # message.clear()
        # message.goto(-screen_width/2+10, screen_height/2-60)
        # message.write(
        #     "Close the window \nto exit",
        #     align="left",
        #     font=("Arial", 16, "bold")
        # )
        # turtle.bye()
        # sc.bye()
        # turtle.done()

    def main_loop():
        global score

        sc.update()
        sc.setup(
            screen_width, 
            screen_height, 
            startx=SCREEN_MID_X-(screen_width/2)+x_offset, 
            starty=SCREEN_MID_Y-(screen_height/2)-y_offset
        )
        update_score()
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
            place_food()

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
        update_score()
        check_collision()
        time.sleep(DELAY)

    def move_food():
        food.goto(x_food-x_offset, y_food-y_offset)

    def place_food():
        gridx = range(int(left) + STEPS, int(right), STEPS)
        gridy = range(int(top) + STEPS, int(bottom), STEPS)

        occupied = {
            tuple(value for value in head.position())
        }

        occupied.update(
            tuple(value for value in segment.position())
            for segment in segments
        )

        available = [
            (x, y)
            for x in gridx
            for y in gridy
            if (x, y) not in occupied
        ]

        if not available:
            return False

        global x_food
        global y_food
        x_food, y_food = random.choice(available)

        return True

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
    sc.onkeypress(exit_game, "Escape")

    welcome()
    try:
        while not game_end:
            if (direction != "stop"):
                main_loop()
    except (turtle.Terminator, tk.TclError):
        pass
    sc.reset()
    sc.bye()