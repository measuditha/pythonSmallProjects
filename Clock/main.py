import turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=500, height=500)
screen.title("Clock")
screen.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(hr, mn, sec, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("black")
    pen.pendown()
    pen.circle(210)

    # Draw the dots with numbers
    def draw_number_dot(angle, color, num):
        pen.up()
        pen.goto(0, 0)
        pen.setheading(90)
        pen.rt(angle)
        pen.fd(170)
        pen.color(color)
        pen.begin_fill()
        pen.circle(8)
        pen.end_fill()
        pen.color("black")

        # Adjust the position of the numbers
        if num < 10:
            pen.goto(pen.xcor() - -5, pen.ycor() - 25)  # Adjusted position
        else:
            pen.goto(pen.xcor() - 7, pen.ycor() - 25)  # Adjusted position

        pen.write(str(num), align="center", font=("Arial", 8, "normal"))

    for i in range(1, 13):
        angle = i * 30
        if i in [3, 6, 9, 12]:
            draw_number_dot(angle, "red", i)
        else:
            draw_number_dot(angle, "blue", i)

    # Draw the hands
    hands = [("green", 125, 12), ("red", 150, 60), ("black", 200, 60)]
    time_set = (hr, mn, sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])

 # Add 'CDU' text under the 12 number
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.rt(-3)  # Angle for the 12 number
    pen.fd(120)  # Adjusted position
    pen.color("red")
    pen.write("CDU", align="center", font=("Arial", 12, "bold"))
    pen.color("black")  # Reset color

while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    draw_clock(hr, mn, sec, pen)
    screen.update()
    time.sleep(1)
    pen.clear()

screen.mainloop()