import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
angles = [0, 90, 180, 270]

# RANDOM WALK SEGMENT ---------------------------------------------------
def random_color():
	r = random.randint(1, 255)
	g = random.randint(1, 255)
	b = random.randint(1, 255)
	return r, g, b

def random_walk(steps):
	for step in range(steps):
		tim.color(random_color())
		blocks = random.randint(5, 15)
		angle = random.choice(angles)
		tim.setheading(angle)
		tim.fd(blocks)

tim.pensize(10)
tim.speed("fastest")
random_walk(200)

screen = t.Screen()
screen.exitonclick()
