
from turtle import Turtle
from typing_extensions import Self

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = Self.ycor() + 20
        Self.goto(Self.xcor(), new_y)

    def go_down(self):
        new_y = Self.ycor() - 20
        Self.goto(Self.xcor(), new_y)


