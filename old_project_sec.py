
from cs1graphics import *

# Program Author and Description
print("\tProgram Desc.: Draw a red circle which starts with radius 0 and expands. Choose a change in radius"
      "\n\t\t\tthat makes a nice visual effect and assume that the maximum radius is 150 pixels long. "
      "\n\t\t\tThe circle must be drawn at the center of the canvas."
      "\n\tDeveloper: Robert \n\tDate created: "
      "11/10/2020")

# Create a window and set: BackgroundColor,Height,Width, and Title properties
window = Canvas()
window.setBackgroundColor("white")
window.setHeight(600)
window.setWidth(900)
window.setTitle("Question #2")


circleRadius = 1
while circleRadius < 150:
    # Draw redCircle with setFillColor("red")
    redCircle = Circle(circleRadius, Point(450, 300))  # circleRadius,  Point(450, 300)
    redCircle.setFillColor("black")
    circleRadius += 2               # Increase circleRadius by 1
    window.add(redCircle)  # Redraw redCircle to the window