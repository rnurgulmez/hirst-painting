# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 30)
#
# # we need it in a clean format like (r, g, b) not like rgb(r = , g= , b= )
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random
# We specified which color mode we would use
turtle_module.colormode(255)
# object created
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
              (251, 248, 243), (243, 223, 231), (235, 243, 237), (214, 226, 242),
              (158, 187, 177), (201, 164, 191), (208, 212, 168), (166, 193, 211),
              (207, 180, 200), (176, 199, 191), (166, 195, 218), (163, 199, 218)
              ]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# We created a screen object from the Screen class
screen = turtle_module.Screen()
# then we finally can use its methods
screen.exitonclick()