# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_new = []
# for i in colors:
#     color_new.append((i.rgb.r,i.rgb.g,i.rgb.b))
# print(color_new)
import random

rgb_list = [(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

import turtle as t

t.speed("fastest")
t.colormode(255)
for i in range(10):
    for _ in range(10):
        t.color(random.choice(rgb_list))
        t.dot(20)
        t.penup()
        t.forward(50)
        t.pendown()
    t.penup()
    t.goto(0,70*(i+1))
    t.pendown()

screen = t.Screen()
screen.exitonclick()