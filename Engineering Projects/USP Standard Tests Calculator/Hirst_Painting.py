# Importing Colors from an image
# import colorgram as cg
#
# # Extract 6 colors from an image.
# colors = cg.extract('hirst.jpg', 50)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


# removed the first 4 background colors
color_list = [(196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154),
              (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10),
              (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 215),
              (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238), (100, 226, 236), (243, 164, 155),
              (170, 175, 240), (252, 6, 60), (5, 245, 224)]

from tkinter import *
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# tim.reset()
tim.speed("fastest")

x = 0
y = 0
for y in range(10):
	for x in range(10):
		tim.pd()
		tim.color(random.choice(color_list))
		tim.begin_fill()
		tim.circle(20)
		tim.end_fill()
		tim.pu()
		tim.fd(50)
	tim.setx(0)
	tim.sety(50 * (y + 1))
tim.ht()

screen = t.Screen()
screen.exitonclick()
# ts = t.getscreen()
# ts.getcanvas().postscript(file="test.eps")
