
import turtle as t
import random

tim = t.Turtle()

colours = ["CornFlowerBlue", "DarkOrchid", "LightSeaGreen", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
