from cs1graphics import *

# Program Author and Description
print("\tProgram Desc.: Drawing of a face (keep it short and simple!)"
      "\n\tDeveloper: Robert \n\tDate created: "
      "11/10/2020")

# Create a window and set: BackgroundColor,Height,Width, and Title properties
window = Canvas()
window.setBackgroundColor("black")
window.setHeight(600)
window.setWidth(900)
window.setTitle("Question #1")

# Draw face with setFillColor("yellow")
face = Circle(250, Point(450, 300))         # Radius: 250,  Point(450, 300)
face.setFillColor("green")
window.add(face)  # Add face to the window

# Draw leftEye and set: Height,Width,setFillColor properties
leftEye = Ellipse()
leftEye.setWidth(100)
leftEye.setHeight(50)
leftEye.moveTo(350, 200)
leftEye.setFillColor("blue")
window.add(leftEye)         # Add leftEye to the window

# Draw rightEye and set: Height,Width,setFillColor properties
rightEye = Ellipse()
rightEye.setWidth(100)
rightEye.setHeight(50)
rightEye.moveTo(550, 200)
rightEye.setFillColor("blue")
window.add(rightEye)         # Add rightEye to the window

# Draw mouth with setFillColor("blue")
mouth = Circle(50, Point(450, 400))         # Radius: 50,  Point(450, 400)
mouth.setFillColor("blue")
window.add(mouth)  # Add mouth to the window