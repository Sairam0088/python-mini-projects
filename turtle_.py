import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing Pad")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off animation

# Create the pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)

# Function to handle pen movement
def drag(x, y):
    pen.ondrag(None)  # Disable event binding during dragging
    pen.setheading(pen.towards(x, y))
    pen.goto(x, y)
    pen.ondrag(drag)  # Re-enable event binding after dragging

# Event binding for mouse dragging
pen.ondrag(drag)

# Function to change pen color to red
def change_color_red():
    pen.color("red")

# Function to change pen color to green
def change_color_green():
    pen.color("green")

# Function to change pen color to blue
def change_color_blue():
    pen.color("blue")

# Function to clear the drawing
def clear_drawing():
    pen.clear()

# Event binding for changing pen color
screen.listen()
screen.onkeypress(change_color_red, "r")
screen.onkeypress(change_color_green, "g")
screen.onkeypress(change_color_blue, "b")

# Event binding for clearing drawing
screen.onkeypress(clear_drawing, "c")

# Main loop
while True:
    screen.update()  # Update the screen continuously

# Keep the window open
screen.mainloop()
