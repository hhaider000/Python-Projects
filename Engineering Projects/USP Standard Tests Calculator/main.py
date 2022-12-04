from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["gray", "blue", "green", "red", "alice blue", "brown", "orange", "black", "teal", "cyan", "chocolate",
          "blue violet", "magenta"]


# DRAW SHAPES SEGMENT ---------------------------------------------------
def draw_shape(num_sides):
	angle = float(360 / num_sides)
	for i in range(num_sides):
		tim.right(angle)
		tim.fd(100)


for i in range(3, 9):
	tim.color(random.choice(colors))
	draw_shape(i)

screen = Screen()
screen.exitonclick()
