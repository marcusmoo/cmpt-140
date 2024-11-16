import turtle

a = turtle.Turtle()

running = True

a.penup()
while running:

    a.goto(-800, -600)
    a.goto(800, 600)

input("Enter any value to end the program: ")

