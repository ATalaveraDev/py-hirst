import turtle as turtle_module
import random
from color_palette import get_colors

turtle_module.colormode(255)

colors = get_colors("mario.png")

turt = turtle_module.Turtle()

turt.penup()
turt.ht()
turt.setheading(225)
turt.forward(250)
turt.setheading(0)

for index in range(1, 101):
  turt.dot(10, random.choice(colors))
  turt.forward(50)
  if index % 10 == 0:
    turt.setheading(90)
    turt.forward(50)
    turt.setheading(180)
    turt.forward(500)
    turt.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()