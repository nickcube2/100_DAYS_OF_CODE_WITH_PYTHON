from re import T
from turtle import Screen, Turtle, exitonclick

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

def square():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.down(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.up(100)

print(square())






screen = Screen()
screen = exitonclick()