import turtle
from turtle import *

turtle.title("Rainbow Spiral!!!")
speed(14)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g= g + 3
    elif i<255*2//3:
        r= r - 3
    elif i<255:
        b= b + 3
    elif i<255*4//3:
        r= r + 3
    elif i<255*5//3:
        r= r + 3
    else:
        b= b - 3

    fd(50+i)
    rt(91)
    pencolor(r,g,b)

turtle.done()