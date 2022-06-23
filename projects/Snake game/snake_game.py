import turtle
import math
import time
import random

delay = 0.1

# Score
score = 0
score2 = 0
high_score = 0
high_score2 = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off the screen updates

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(100, 0)
head.direction = "stop"

# Snake head 2
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("yellow")
head2.penup()
head2.goto(-100, 0)
head2.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


# Snake Food 2
food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("blue")
food2.penup()
food2.goto(100, 100)
segments = []
segments2 = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("P1 - Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Pen 2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -260)
pen2.write("P2 - Score: 0 High score: 0", align="center", font=("Courier", 24, "normal"))

# Pen 3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.shape("square")
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, 0)


# Functions

# start game
def start_game():
    global game_state
    game_state = "game"


# For Player 1
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


# For Player 2
def go_up2():
    if head2.direction != "Down":
        head2.direction = "Up"


def go_down2():
    if head2.direction != "Up":
        head2.direction = "Down"


def go_left2():
    if head2.direction != "Right":
        head2.direction = "Left"


def go_right2():
    if head2.direction != "Left":
        head2.direction = "Right"


def move2():
    if head2.direction == "Up":
        y = head2.ycor()
        head2.sety(y + 20)
    if head2.direction == "Down":
        y = head2.ycor()
        head2.sety(y - 20)
    if head2.direction == "Left":
        x = head2.xcor()
        head2.setx(x - 20)
    if head2.direction == "Right":
        head2.setx(head2.xcor() + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(start_game, "e")

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

wn.listen()
wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_right2, "Right")
wn.onkeypress(go_left2, "Left")

game_state = "splash"

time_limit = 60
start_time = time.time()
print(start_time)

# Main Game loop
while True:

    if game_state == "splash":
        wn.bgpic("splash.png")
        head.hideturtle()
        head2.hideturtle()
        food.hideturtle()

    elif game_state == "game":
        wn.bgpic("space.png")
        head.showturtle()
        head2.showturtle()
        food.showturtle()

        # Timer
        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            game_state = "game_over"
            print("GAME OVER")
            pen.clear()
            pen2.clear()

            # show who wins
            if high_score > high_score2:
                pen3.write("Player One wins", align="center", font=("Courier", 30, "normal"))
            elif high_score2 > high_score:
                pen3.write("Player Two wins", align="center", font=("Courier", 30, "normal"))
            time.sleep(5)

    elif game_state == "game_over":
        wn.bgpic("gameover.png")
        # Reset everything for player one
        head.goto(100, 0)
        head.direction = "stop"
        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments list
        segments.clear()
        # reset the score
        score = 0
        # reset delay
        delay = 0.1
        # Reset everything for player two
        head2.goto(-100, 0)
        head2.direction = "stop"
        # hide segments
        for segment2 in segments2:
            segment2.goto(1000, 1000)
        # clear the segments list
        segments2.clear()
        # reset the score
        score2 = 0
        # reset delay
        delay = 0.1

        game_state = "game"

    wn.update()
    # Check for a collision with the border for Player 1
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(100, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("P1 - Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for a collision with the border for Player 2
    if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 290 or head2.ycor() < -290:
        time.sleep(1)
        head2.goto(-100, 0)
        head2.direction = "stop"

        # Hide the segments
        for segment2 in segments2:
            segment2.goto(1000, 1000)

        # Clear the segments list
        segments2.clear()

        # Reset the score
        score2 = 0

        # Reset the delay
        delay = 0.1

        pen2.clear()
        pen2.write("P2 - Score: {} High Score: {}".format(score2, high_score2), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food for Player 1

    if head.distance(food) < 20:
        # Move the food to random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("P1 - Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food 2 for Player 1

    if head.distance(food2) < 20:
        # Move the food to random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food2.goto(x, y)

        # Remove a segment
        segments[-1].goto(1000, 1000)
        # Remove it from list
        segments.remove(segments[-1])

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score -= 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("P1 - Score: {} High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check for a collision with the food for Player 2
    if head2.distance(food) < 20:
        # Move the food to random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        # Add a segment
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color("grey")
        new_segment2.penup()
        segments2.append(new_segment2)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score2 += 10

        if score2 > high_score2:
            high_score2 = score2

        pen2.clear()
        pen2.write("P2 - Score: {} High Score: {}".format(score2, high_score2), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments2) - 1, 0, -1):
        x = segments2[index - 1].xcor()
        y = segments2[index - 1].ycor()
        segments2[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x, y)

    # Check for a collision with the food 2 for Player 2

    if head2.distance(food2) < 20:
        # Move the food to random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food2.goto(x, y)

        # Remove a segment
        segments2[-1].goto(1000, 1000)
        # Remove it from list
        segments2.remove(segments2[-1])

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score2 -= 10

        if score2 > high_score2:
            high_score2 = score2

        pen2.clear()
        pen2.write("P2 - Score: {} High Score: {}".format(score2, high_score2), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments2) - 1, 0, -1):
        x = segments2[index - 1].xcor()
        y = segments2[index - 1].ycor()
        segments2[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x, y)

    move()
    move2()

    # Check for head collision with body segments for Player 1
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("P1 - Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for head collision with body segments for Player 2
    for segment2 in segments2:
        if segment2.distance(head2) < 20:
            time.sleep(1)
            head2.goto(0, 0)
            head2.direction = "stop"

            # Hide the segments
            for segment2 in segments2:
                segment2.goto(1000, 1000)

            # Clear the segments list
            segments2.clear()

            # Reset the score
            score2 = 0

            # Reset the delay
            delay = 0.1

            pen2.clear()
            pen2.write("P2 - Score: {} High Score: {}".format(score2, high_score2), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
