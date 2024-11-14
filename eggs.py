print("Hello, World!")
import turtle

def draw_bacon():
    turtle.color("brown")
    turtle.begin_fill()
    
    # Draw the bacon strip
    turtle.forward(100)  # Move forward to draw the length of the bacon
    turtle.right(30)     # Turn right to create a curve
    turtle.forward(20)   # Move forward to create the curve
    turtle.right(30)     # Turn right again
    turtle.forward(100)  # Draw the other side of the bacon
    turtle.right(30)     # Turn to close the shape
    turtle.forward(20)   # Complete the curve
    turtle.right(30)     # Turn to finish the strip
    turtle.forward(100)  # Draw the last side of the bacon
    turtle.end_fill()

# Set up the turtle environment
turtle.speed(1)  # Set the speed of drawing
draw_bacon()     # Call the function to draw the bacon
turtle.done()    # Finish the drawing
if turtle.speed() > 5:
    print("The turtle is moving fast!")
else:
    print("The turtle is moving slow.")
