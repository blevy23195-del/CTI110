# P4LAB1_LevyBarry.py
# Barry Levy
# Date : March 22, 2026
# Assignment: P4LAB1
# Description: Write a turtle graphics programs that draws a triangle and a square using loops

import turtle
# Set up the window (the stage)
win = turtle.Screen()
win.bgcolor("skyblue")      # Change this to any color like "lightgray" or "navy"

# Set up the turtle (the pen)
t = turtle.Turtle()
t.shape("turtle")           # Makes the cursor look like an actual turtle
t.color("darkorange")       # Change this to your favorite color
t.pensize(3)                # Makes the lines a bit thicker and easier to see
t.speed(2)                  # 1 is slow, 10 is fast

# --- DRAW THE SQUARE BASE ---
# Using a for loop to repeat the side and turn 4 times
t.begin_fill()
for i in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# Move the turtle to the top-left corner of the square
t.left(90)
t.forward(150)
t.right(90)  

# --- DRAW THE TRIANGLE ROOF ---
# A triangle has 3 sides and 120-degree angles
# --- DRAW THE FILLED TRIANGLE ROOF ---
t.fillcolor("darkred")  # Optional: Pick a specific roof color
t.begin_fill()          # Start the fill here

sides_drawn = 0
while sides_drawn < 3:
    t.forward(150)
    t.left(120)
    sides_drawn += 1

t.end_fill()            # Stop the fill here
win.mainloop()