import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.reset()
tim.speed("fastest")


def random_color():
	r = random.randint(1, 255)
	g = random.randint(1, 255)
	b = random.randint(1, 255)
	return r, g, b


def draw_spirograph(gapsize):
	for i in range(int(360 / gapsize)):
		tim.color(random_color())
		tim.circle(100)
		tim.setheading(tim.heading() + gapsize)

user = int(input("Provide a number between 1 and 20: "))
draw_spirograph(user)
screen = t.Screen()
screen.exitonclick()
