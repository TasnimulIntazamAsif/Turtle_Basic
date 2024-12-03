import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.title("ASIF")
screen.bgcolor("white")

# Create and setup the turtle
t = turtle.Turtle()
t.speed(3)  # Set moderate speed for smooth animation
t.pensize(5)
t.color("blue")
t.penup()
t.goto(-200, 0)  # Starting position
t.pendown()

# Function to draw letter A
def draw_A():
    t.left(70)
    t.forward(100)
    t.right(140)
    t.forward(100)
    t.backward(40)
    t.right(110)
    t.forward(35)
    t.penup()
    t.goto(t.xcor() + 40, 0)  # Move to next letter position
    t.left(80)
    t.pendown()

# Function to draw letter S
def draw_S():
    t.penup()
    t.goto(t.xcor(), 50)  # Start from top
    t.pendown()
    t.setheading(180)  # Face left
    t.forward(30)
    t.backward(30)
    t.right(90)
    t.circle(-20, 180)  # Top curve
    t.circle(20, 180)   # Bottom curve
    t.forward(30)
    t.penup()
    t.goto(t.xcor() + 60, 0)  # Move to next letter position
    t.pendown()

# Function to draw letter I
def draw_I():
    t.penup()
    t.goto(t.xcor(), 50)  # Start from top
    t.pendown()
    t.setheading(0)
    t.forward(30)
    t.backward(15)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(15)
    t.forward(30)
    t.penup()
    t.goto(t.xcor() + 40, 0)  # Move to next letter position
    t.pendown()

# Function to draw letter F
def draw_F():
    t.penup()
    t.goto(t.xcor(), 50)  # Start from top
    t.pendown()
    t.setheading(270)  # Face down
    t.forward(100)
    t.backward(100)
    t.setheading(0)  # Face right
    t.forward(40)
    t.backward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(35)

# Draw the letters
draw_A()
draw_S()
draw_I()
draw_F()

# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
