from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)


screen.exitonclick()