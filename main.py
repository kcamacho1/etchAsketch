from turtle import Turtle, Screen

gert = Turtle()
screen = Screen()


# Gert moves forwards 10 paces
def move_forwards():
    gert.forward(10)


# Gert moves back 10 paces but doesn't rotate
def move_backwards():
    gert.backward(10)


# fuction to clear etch-A-sketch screen
def clear_screen():
    gert.clear()


# function to face left
def turn_left():
    gert.left(10)


# function to face right
def turn_right():
    gert.right(10)


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)    gert.right(10)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.exitonclick()
